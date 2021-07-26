from sanic import Sanic


class HTTPService:
    def __init__(self, routes):
        self.app = Sanic()
        self.register()

    def start(self):
        self.app.run()
