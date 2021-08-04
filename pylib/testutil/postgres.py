from pylib.postgres import Postgres
import docker
import time


def clear_table(table_name):
    with Postgres.repo() as cursor:
        cursor.execute(f"truncate {table_name}")

def run():
    client = docker.from_env()
    test_cfg = {
        "POSTGRES_HOST": "localhost",
        "POSTGRES_USER": "test-user",
        "POSTGRES_PASSWORD": "test-password",
        "POSTGRES_DB": "test-db"
    }
    container = client.containers.run(
        "postgres:latest",
        name="test-postgres",
        environment=test_cfg,
        ports={'5432/tcp': 5432},
        publish_all_ports=True,
        detach=True,
    )
    while True:
        try:
            Postgres.setup(test_cfg)
            Postgres.migrate("up")
            break
        except Exception:
            time.sleep(1)
    return test_cfg, container

def stop(container):
    container.remove(v=True, force=True)