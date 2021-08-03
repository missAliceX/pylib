import psycopg2 
from psycopg2.pool import SimpleConnectionPool
from contextlib import contextmanager
import os
import logging
import time
import asyncio
from os import path

log = logging.getLogger(__name__)
migrations_dir = path.join(path.dirname(path.realpath(__file__)), 'migrations')


class Postgres:
    @classmethod
    def create_pool(cls, cfg):
        cls.pool = SimpleConnectionPool(
            1, 20,
            host=cfg["postgres_host"],
            database=cfg["postgres_db"],
            user=cfg["postgres_user"],
            password=cfg["postgres_password"]
        )
        log.info("Connected to Postgres pool")

    @classmethod
    async def connect(cls, cfg):
        cls.create_pool(cfg)
        while True:
            try:
                conn = cls.pool.getconn()
                cur = conn.cursor()
                cur.execute('SELECT 1')
            except psycopg2.OperationalError:
                log.error("get connection from pool")
                cls.create_pool(cfg)
            await asyncio.sleep(60)

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