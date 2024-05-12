from lib.utils.cli import CLI

from lib.commands.run_server import run_server
from lib.commands.run_worker import run_worker

cli = CLI(commands=[
    run_server, run_worker
])

