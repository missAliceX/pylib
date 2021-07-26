from concurrent.futures import ThreadPoolExecutor
import grpc

class GRPCService:
    def __init__(self, register, ServiceClass):
        self.server = grpc.server(ThreadPoolExecutor(max_workers=10))
        register(ServiceClass(), self.server)

    def start(self, register, ServiceClass):
        self.server.add_insecure_port("[::]:9090")
        self.server.start()
        self.server.wait_for_termination()