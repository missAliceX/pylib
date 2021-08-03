from psycopg2.pool import SimpleConnectionPool
from contextlib import contextmanager
import os
import logging
import time
from os import path

log = logging.getLogger(__name__)
migrations_dir = path.join(path.dirname(path.realpath(__file__)), 'migrations')


class Postgres:
    pool = None
    cfg = None

    @classmethod
    def connect(cls, cfg):
        if cls.pool is None:
            cls.cfg = cfg
            cls.pool = SimpleConnectionPool(
                1, 20,
                host=cfg["postgres_host"],
                database=cfg["postgres_db"],
                user=cfg["postgres_user"],
                password=cfg["postgres_password"]
            )
            log.info("Connected to Postgres pool")

    @classmethod
    @contextmanager
    def repo(cls, commit=True):
        while True:
            try:
                conn = cls.pool.getconn()
                break
            except:
                log.error("get connection from pool")
                cls.pool = None
                cls.connect(cls.cfg)
                time.sleep(10)

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