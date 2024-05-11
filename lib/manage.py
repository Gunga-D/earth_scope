from lib.utils.cli import CLI

from lib.commands.load_fdsn import load_fdsn
from lib.commands.run_loader import run_loader
from lib.commands.run_server import run_server
from lib.commands.run_worker import run_worker

cli = CLI(commands=[
    run_loader, load_fdsn, run_server, run_worker
])

