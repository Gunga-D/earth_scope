import logging
from lib.config import settings

def configure_logging():
    logging.root.setLevel(settings['logger']['level'])

def get_product_logger() -> logging.Logger:
    return logging.getLogger(settings['logger']['name'])