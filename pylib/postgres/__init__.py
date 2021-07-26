from psycopg2.pool import SimpleConnectionPool
from contextlib import contextmanager
import os
import logging
from os import path

log = logging.getLogger(__name__)
migrations_dir = path.join(path.dirname(path.realpath(__file__)), 'migrations')


class Postgres:
    pool = None

    @classmethod
    def connect(cls, cfg):
        if cls.pool is None:
            cls.pool = SimpleConnectionPool(
                1, 20,
                host=cfg["postgres_host"],
                database=cfg["postgres_db"],
                user=cfg["postgres_user"],
                password=cfg["postgres_password"]
            )
            log.info("connected to Postgres pool")

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
            log.error("executing query")
            raise
        finally:
            cls.pool.putconn(conn)

    @classmethod
    def migrate(cls, mode):
        log.info(f"starting migrate {mode}...")
        with cls.repo() as cursor:
            for root, dirs, files in os.walk(migrations_dir):
                for file in files:
                    if file.endswith(f'.{mode}.sql'):
                        cursor.execute(open(os.path.join(root, file)).read())
        log.info(f"migrate {mode} complete.")