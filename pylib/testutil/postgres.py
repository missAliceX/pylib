from pylib.postgres import Postgres
import docker

def clear_table(table_name):
    with Postgres.repo() as cursor:
        cursor.execute(f"truncate {table_name}")

def run():
    client = docker.from_env()
    test_cfg = {
        "POSTGRES_USER": "test-user",
        "POSTGRES_PASSWORD": "test-password",
        "POSTGRES_DB": "test-db"
    }
    return test_cfg, client.containers.run(
        "postgres",
        name="test-postgres",
        environment=test_cfg,
        detach=True,
    )

def stop(container):
    container.remove(v=True, force=True)