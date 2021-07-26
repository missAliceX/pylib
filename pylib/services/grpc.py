import futures
import grpc

class GRPCService:
    def __init__(self):
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    def start(self, register, ServiceClass):
        register(ServiceClass(), self.server)
        self.server.add_insecure_port("[::]:9090")
        self.server.start()
        self.server.wait_for_termination()