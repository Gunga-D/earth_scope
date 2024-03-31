import click
from typing import List

from lib.commands import stream_handler, fetch_channels
from lib.interactions.ipgp import IPGPClient
from lib.services.ipgp import IPGPService
from lib.config import SAVING_PATH

@click.command()
@click.option('--url', default='http://ws.ipgp.fr/fdsnws', help='Base url of ipgp client', type=(click.STRING))
@click.option('--channel', default=['G/CCD', 'PF/CAS'], multiple=True, help='Receive channels in format [network]/[station]')
def load_ipgp(url, channel: List[str]) -> None:
    """Start loading data only from ipgp.
    Usage: cli.py load_ipgp --url=http://ws.ipgp.fr/fdsnws --channel G/CCD --channel PF/CAS
    """
    try:
        channels = fetch_channels(channel)
    except Exception as e:
        click.echo(f"ERROR: cannot fetch channels: {e}")
        return

    client = IPGPClient(url)
    service = IPGPService(channels, client, stream_handler('ipgp', SAVING_PATH))
    try:
        service.run()
    except (KeyboardInterrupt, SystemExit):
        click.echo('INFO: closed the programm')