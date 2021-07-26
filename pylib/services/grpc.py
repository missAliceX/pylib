from concurrent.futures import ThreadPoolExecutor
import grpc
import logging
import os

logging.basicConfig(
    format='[%(asctime)s] [%(process)d] [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S %z',
    level=os.getenv("LOG_LEVEL", logging.DEBUG),
)

log = logging.getLogger(__name__)

class GRPCService(Service):
    def __init__(self, name, ServiceClass, register, cfg={}):
        super().__init__(cfg)
        self.name = name
        self.server = grpc.server(ThreadPoolExecutor(max_workers=10))
        register(ServiceClass(), self.server)

    def start(self):
        self.server.add_insecure_port("[::]:9090")
        self.server.start()
        log.info(f"started grpc service: {self.name}")
        self.server.wait_for_termination()