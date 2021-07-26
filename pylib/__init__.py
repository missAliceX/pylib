import logging
import os

logging.basicConfig(
    format='[%(asctime)s] [%(process)d] [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S %z',
    level=os.getenv("LOG_LEVEL", logging.DEBUG),
)