from lib.utils.cli import CLI

from lib.commands.load_iris import load_iris
from lib.commands.load_ipgp import load_ipgp
from lib.commands.load_geofon import load_geofon
from lib.commands.run_loader import run_loader

cli = CLI(commands=[
    load_iris, load_ipgp, load_geofon, run_loader
])

