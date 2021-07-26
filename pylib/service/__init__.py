from pylib.postgres import Postgres

class Service:
    def __init__(self, cfg):
        Postgres.connect(cfg)
        Postgres.migrate("up")