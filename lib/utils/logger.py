import logging
from lib.config import settings
import sys

def configure_logging():
    logging.root.setLevel(settings['logger']['level'])
    
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(settings['logger']['format'])
    handler.setFormatter(formatter)
    logging.root.addHandler(handler)

def get_product_logger() -> logging.Logger:
    return logging.getLogger(settings['logger']['name'])