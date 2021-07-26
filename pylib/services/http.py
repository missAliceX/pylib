from sanic import Sanic


class HTTPService:
    def __init__(self, name, routes):
        self.app = Sanic(name)
        self.register()

    def start(self):
        self.app.run()
