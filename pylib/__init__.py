import logging
import os

# This prevents sanic from logging twice when we mix in our custom logs
logging.getLogger("sanic.access").propagate = False
logging.getLogger("sanic.root").propagate = False
logging.basicConfig(
    format='[%(asctime)s] [%(process)d] [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S %z',
    level=os.getenv("LOG_LEVEL", logging.DEBUG),
)