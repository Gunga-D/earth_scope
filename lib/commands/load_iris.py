import click
from typing import List

from lib.commands import trace_handler, fetch_channels
from lib.config import SAVING_PATH
from lib.interactions.iris import IrisClient

@click.command()
@click.option('--port', default=18000, help='Seedlink port to load the data', type=(click.INT))
@click.option('--host', default='rtserve.iris.washington.edu', help='Seedlink host to load the data', type=(click.STRING))
@click.option('--channel', default=['YN/SGBS2', 'XL/MG04', 'WY/YGC'], multiple=True, help='Receive channels in format [network]/[station]')
def load_iris(port, host, channel: List[str]) -> None:
    """Start loading data only from iris.edu.
    Usage: cli.py load_iris --port=18000 --host=rtserve.iris.washington.edu --channel YN/SGBS2 --channel XL/MG04 --channel WY/YGC
    """
    try:
        channels = fetch_channels(channel)
    except Exception as e:
        click.echo(f"ERROR: cannot fetch channels: {e}")
        return

    client = IrisClient(host, str(port), channels, trace_handler('iris', SAVING_PATH))
    try:
        client.run()
    except (KeyboardInterrupt, SystemExit):
        click.echo('INFO: closed the programm')