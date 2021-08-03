from sanic import Sanic


class HTTPService:
    def __init__(self, name="demo", cfg={}):
        self.app = Sanic(name)
        self.register()

    def start(self):
        self.app.run()
