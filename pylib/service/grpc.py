from concurrent.futures import ThreadPoolExecutor
import grpc
import logging
import os

log = logging.getLogger(__name__)

class GRPCService:
    def __init__(self, name, add_servicer_to_server):
        self.name = name

        # Creates a gRPC server with workers
        self.server = grpc.server(ThreadPoolExecutor(max_workers=10))
        self.server.add_insecure_port("[::]:50051")

        # Adds the gRPC handlers and routes to the server
        add_servicer_to_server(self, self.server)

    def start(self):
        # Starts the server
        self.server.start()
        log.info(f"Started gRPC service \"{self.name}\" on :50051")
        self.server.wait_for_termination()
