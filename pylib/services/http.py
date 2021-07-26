from sanic import Sanic

class HTTPService:
    def __init__(self, routes):
        self.app = Sanic()
        routes.register(self.app)

    def start(self):
        self.app.run()