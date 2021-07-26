from concurrent.futures import ThreadPoolExecutor
import grpc
import logging

log = logging.getLogger(__name__)

class GRPCService:
    def __init__(self, name, ServiceClass, register):
        self.name = name
        self.server = grpc.server(ThreadPoolExecutor(max_workers=10))
        register(ServiceClass(), self.server)

    def start(self):
        self.server.add_insecure_port("[::]:9090")
        self.server.start()
        log.info(f"started grpc service: {self.name}")
        self.server.wait_for_termination()