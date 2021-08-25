from sanic import Sanic


class HTTPService:
    def __init__(self, name="demo"):
        # Creates a Sanic HTTP server
        self.app = Sanic(name)

        # Adds the HTTP handlers and routes to the Sanic server
        self.register()

    def start(self):
        # Starts the server
        self.app.run(host="0.0.0.0", port=8080)
