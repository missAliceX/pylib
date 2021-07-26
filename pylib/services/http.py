from sanic import Sanic

class HTTPService:
    def __init__(self):
        self.app = Sanic()

    def start(self, routes):
        routes.register(self.app)
        self.app.run()