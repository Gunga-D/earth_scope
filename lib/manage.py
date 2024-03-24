from lib.utils.logger import configure_logging
from lib.utils.cli import CLI

from lib.commands.load_iris import load_iris
from lib.commands.run_loader import run_loader

configure_logging()

cli = CLI(commands=[
    load_iris, run_loader
])

