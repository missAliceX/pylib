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
    def connect(cls, cfg, max_retry=5):
        # Try connecting to Postgres
        for retry_count in range(max_retry):
            try:
                cls.pool = ThreadedConnectionPool(
                    1, 20,
                    host=cfg["POSTGRES_HOST"],
                    database=cfg["POSTGRES_DB"],
                    user=cfg["POSTGRES_USER"],
                    password=cfg["POSTGRES_PASSWORD"]
                )
                # try sending some command to the databasee to test the connection
                conn = cls.pool.getconn()
                cur = conn.cursor()
                cur.execute('SELECT 1')
                log.info("connected to postgres")
                return
            except Exception:
                log.error("connect to postgres", exc_info=True)
                retry_count += 0
                
            time.sleep(int(math.exp(retry_count))) # Sleep for an expotentially increasing amount

        # If it still fails, raise an exception
        raise Exception("unable to connect to postgres")

    @classmethod
    @contextmanager
    def repo(cls, commit=True):
        # Grabs a connection from the pool
        conn = cls.pool.getconn()
        try:
            # Gives the cursor as a context to the user so the user can execute queries
            yield conn.cursor()

            # Commit the database transaction after the cursor returns from the context
            if commit:
                conn.commit()
        except Exception:
            # If the user runs a failing query, it will rollback the transaction
            conn.rollback()
            log.error("executing query", exc_info=True)
            raise
        finally:
            # Return the connection to the pool
            cls.pool.putconn(conn)

    @classmethod
    def migrate(cls, mode, dir_path=migrations_dir):
        # Goes through all the files that ends with .up.sql or .down.sql and run the queries inside them
        log.info(f"Starting to migrate {mode} from {dir_path}...")
        with cls.repo() as cursor:
            for root, dirs, files in os.walk(dir_path):
                for file in files:
                    print(file)
                    if file.endswith(f'.{mode}.sql'):
                        log.info(f"Migrating {file}")
                        cursor.execute(open(os.path.join(root, file)).read())
        log.info(f"Migrate {mode} complete.")