import unittest
import docker
import psycopg2
import threading
import mock
import time
from os import path
from pylib.testutil import postgres
from pylib.postgres import PostgresClient, migrations_dir


class PostgresTestCase(unittest.TestCase):
    def setUp(self):
        postgres.stop()

class TestPostgresContainer(PostgresTestCase):
    def test_start_repo_stop(self):
        # Ensures there is no existing container
        client = docker.from_env()
        self.assertRaises(docker.errors.NotFound, client.containers.get, "test-postgres")

        # Start the container, ensure it's there
        _, container = postgres.run()
        self.assertEqual(container, client.containers.get("test-postgres"))

        # Double start the container, make sure it doesn't raise an exception
        test_cfg, container = postgres.run()
        self.assertEqual(container, client.containers.get("test-postgres"))

        # Make sure thee test_cfg can be used to connect
        PostgresClient.connect(test_cfg)

        # Ensure we can run queries
        with postgres.repo() as cursor:
            cursor.execute('SELECT 1')

        # Stop the container, ensure it's no longer there
        postgres.stop()
        self.assertRaises(docker.errors.NotFound, client.containers.get, "test-postgres")


class TestPostgresClient(PostgresTestCase):
    def test_migrate_up(self):
        # Use test migrations instead
        migrations_dir = path.join(path.dirname(path.realpath(__file__)), 'fixtures/migrations')

        # Start the container, connect and migrate
        test_cfg, _ = postgres.run()
        PostgresClient.connect(test_cfg)
        PostgresClient.migrate("up", dir_path=migrations_dir)

        # Check that we can select from the table without raising exceptions
        with PostgresClient.repo() as cursor:
            cursor.execute('select * from examples')

        # Migrate down and ensure that the table is no longer there
        PostgresClient.migrate("down", dir_path=migrations_dir)
        with PostgresClient.repo() as cursor:
            self.assertRaises(psycopg2.errors.UndefinedTable, cursor.execute, 'select * from samples')

        # Stop the container
        postgres.stop()

    @mock.patch("pylib.postgres.time.sleep")
    def test_connect_exponential_backoff(self, sleep):
        # Ensures that the sleep gets longer and eventually raises an exception
        self.assertRaises(Exception, PostgresClient.connect, {}, max_retry=3)
        sleep.assert_has_calls([mock.call(1), mock.call(2), mock.call(7)])
        
