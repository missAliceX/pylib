from pylib.postgres import Postgres

class AutoMigrate:
    def __init__(self, cfg):
        super().__init__(cfg)
        Postgres.connect(cfg)
        Postgres.migrate("up")
