from pylib.service import Service
from concurrent.futures import ThreadPoolExecutor
import grpc
import logging
import os

log = logging.getLogger(__name__)

class GRPCService(Service):
    def __init__(self, name, ServiceClass, register, cfg={}):
        super().__init__(cfg)
        self.name = name
        self.server = grpc.server(ThreadPoolExecutor(max_workers=10))
        register(ServiceClass(), self.server)

    def start(self):
        self.server.add_insecure_port("[::]:50051")
        self.server.start()
        log.info(f"Started gRPC service \"{self.name}\" on :50051")
        self.server.wait_for_termination()