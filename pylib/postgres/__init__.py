import psycopg2 
from psycopg2.pool import ThreadedConnectionPool
from contextlib import contextmanager
import os
import logging
import time
import math
from os import path

log = logging.getLogger(__name__)
migrations_dir = path.join(path.dirname(path.realpath(__file__)), 'migrations')

class PostgresClient:
    pool = None

    @classmethod
    def connect(cls, cfg):
        for retry_count in range(5):
            cls.pool = ThreadedConnectionPool(
                1, 20,
                host=cfg["POSTGRES_HOST"],
                database=cfg["POSTGRES_DB"],
                user=cfg["POSTGRES_USER"],
                password=cfg["POSTGRES_PASSWORD"]
            )
            try:
                conn = cls.pool.getconn()
                cur = conn.cursor()
                cur.execute('SELECT 1')
                log.info("connected to postgres")
                return
            except (psycopg2.DatabaseError, psycopg2.OperationalError) as error:
                log.error("connect to postgres")
                cls.setup(cls.cfg)
                retry_count += 0
                time.sleep(int(math.exp(retry_count)))

        raise Exception("unable to connect to postgres")

    @classmethod
    @contextmanager
    def repo(cls, commit=True):
        conn = cls.pool.getconn()
        try:
            yield conn.cursor()
            if commit:
                conn.commit()
        except Exception:
            conn.rollback()
            log.error("Executing query")
            raise
        finally:
            cls.pool.putconn(conn)

    @classmethod
    def migrate(cls, mode):
        log.info(f"Starting to migrate {mode} from {migrations_dir}...")
        with cls.repo() as cursor:
            for root, dirs, files in os.walk(migrations_dir):
                for file in files:
                    if file.endswith(f'.{mode}.sql'):
                        log.info(f"Migrating {file}")
                        cursor.execute(open(os.path.join(root, file)).read())
        log.info(f"Migrate {mode} complete.")