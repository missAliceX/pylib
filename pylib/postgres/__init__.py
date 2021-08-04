import psycopg2 
from psycopg2.pool import SimpleConnectionPool
from contextlib import contextmanager
import os
import logging
import time
import asyncio
from os import path
from threading import Thread

log = logging.getLogger(__name__)
migrations_dir = path.join(path.dirname(path.realpath(__file__)), 'migrations')
RETRY_DELAY = 60

class Postgres:
    pool = None
    
    @classmethod
    def setup(cls, cfg):
        cls.cfg = cfg
        cls.pool = SimpleConnectionPool(
            1, 20,
            host=cfg["POSTGRES_HOST"],
            database=cfg["POSTGRES_DB"],
            user=cfg["POSTGRES_USER"],
            password=cfg["POSTGRES_PASSWORD"]
        )
        log.info("Connected to Postgres pool")

    @classmethod
    def _connect(cls):
        if cls.pool is None:
            raise Exception("must call setup() first")
        try:
            conn = cls.pool.getconn()
            cur = conn.cursor()
            cur.execute('SELECT 1')
        except psycopg2.OperationalError:
            log.error("get connection from pool")
            cls.setup(cls.cfg)

    @classmethod
    async def connect_async(cls):
        while True:
            cls._connect()
            await asyncio.sleep(RETRY_DELAY)

    @classmethod
    def connect(cls):
        def _run_non_blocking(_cls):
            while True:
                _cls._connect()
                time.sleep(RETRY_DELAY)
        Thread(target=_run_non_blocking, args=(cls,)).start()
        

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