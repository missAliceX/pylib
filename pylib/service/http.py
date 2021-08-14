from sanic import Sanic


class HTTPService:
    def __init__(self, name="demo", cfg={}):
        # Creates a Sanic HTTP server
        self.app = Sanic(name, port=8080)

        # Adds the HTTP handlers and routes to the Sanic server
        self.register()

    def start(self):
        # Starts the server
        self.app.run()
