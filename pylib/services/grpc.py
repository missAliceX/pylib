from concurrent.futures import ThreadPoolExecutor
import grpc

class GRPCService:
    def __init__(self, ServiceClass, register):
        self.server = grpc.server(ThreadPoolExecutor(max_workers=10))
        register(ServiceClass(), self.server)

    def start(self):
        self.server.add_insecure_port("[::]:9090")
        self.server.start()
        self.server.wait_for_termination()