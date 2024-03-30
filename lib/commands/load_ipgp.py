import click
from typing import List
from obspy.core import Stream

from lib.interactions.ipgp import IPGPClient
from lib.services.ipgp import IPGPService
from lib.interactions.entities import Channel

@click.command()
@click.option('--url', default='http://ws.ipgp.fr/fdsnws', help='Base url of ipgp client', type=(click.STRING))
@click.option('--channel', default=['G/CCD'], multiple=True, help='Receive channels in format [network]/[station]')
def load_ipgp(url, channel: List[str]) -> None:
    """Start loading data only from ipgp.
    Usage: cli.py load_ipgp --url=http://ws.ipgp.fr/fdsnws --channel G/CCD
    """
    if len(channel) == 0:
        raise ValueError('There must be at least one channel')
    channels = []
    for raw_channel in channel:
        parsed_channel = raw_channel.split('/')
        if len(parsed_channel) != 2:
            raise ValueError(f'Channel {raw_channel} is not valid. The format [network]/[station]')
        channels.append(Channel(network=parsed_channel[0], station=parsed_channel[1]))
    
    client = IPGPClient(url)
    service = IPGPService(channels, client)

    def log(stream: Stream):
        print(stream)

    service.run(delay=0.5, data_callback=log)
