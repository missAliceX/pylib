import docker
import time

from pylib.postgres import PostgresClient


def run():
    """
    postgres.run starts a Postgres Docker container in the background and returns the test configs
    """
    client = docker.from_env()
    test_cfg = {
        "POSTGRES_HOST": "localhost",
        "POSTGRES_USER": "test-user",
        "POSTGRES_PASSWORD": "test-password",
        "POSTGRES_DB": "test-db"
    }

    try:
        container = client.containers.get("test-postgres")
        container.remove(v=True, force=True)
    except docker.errors.NotFound:
        pass
    
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
            PostgresClient.connect(test_cfg)
            PostgresClient.migrate("up")
            break
        except Exception:
            time.sleep(1)
    return test_cfg, container

def stop():
    """
    postgres.stop stops and removes the given container
    """
    client = docker.from_env()
    try:
        container = client.containers.get("test-postgres")
        container.remove(v=True, force=True)
    except docker.errors.NotFound:
        pass

def repo():
    """
    postgres.repo returns the cursor context for the Docker container
    """
    return PostgresClient.repo()