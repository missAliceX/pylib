from pylib.service import Service
from sanic import Sanic


class HTTPService(Service):
    def __init__(self, name="demo", cfg={}):
        super().__init__(cfg)
        self.app = Sanic(name)
        self.register()

    def start(self):
        self.app.run()
