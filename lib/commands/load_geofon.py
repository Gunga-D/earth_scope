import click
from typing import List

from lib.commands import trace_handler, fetch_channels
from lib.config import SAVING_PATH
from lib.interactions.geofon import GeofonClient
from lib.interactions.entities import Channel

@click.command()
@click.option('--port', default=18000, help='Seedlink port to load the data', type=(click.INT))
@click.option('--host', default='geofon-open.gfz-potsdam.de', help='Seedlink host to load the data', type=(click.STRING))
@click.option('--channel', default=['GE/SFJD', 'GE/PUL'], multiple=True, help='Receive channels in format [network]/[station]')
def load_geofon(port, host, channel: List[str]) -> None:
    """Start loading data only from geofon.
    Usage: cli.py load_geofon --port=18000 --host=geofon-open.gfz-potsdam.de --channel WLF/GE
    """
    try:
        channels = fetch_channels(channel)
    except Exception as e:
        click.echo(f"ERROR: cannot fetch channels: {e}")
        return

    client = GeofonClient(host, str(port), channels, trace_handler('geofon', SAVING_PATH))
    try:
        client.run()
    except (KeyboardInterrupt, SystemExit):
        click.echo('INFO: closed the programm')