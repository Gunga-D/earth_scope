import click
from typing import List
from lib.interactions.iris.client import IrisClient
from lib.interactions.entities import Channel

@click.command()
@click.option('--port', default=18000, help='Seedlink port to load the data', type=(click.INT))
@click.option('--host', default='rtserve.iris.washington.edu', help='Seedlink host to load the data', type=(click.STRING))
@click.option('--channel', default=['YN/SGBS2', 'XL/MG04', 'WY/YGC'], multiple=True, help='Receive channels in format [network]/[station]')
def load_iris(port, host, channel: List[str]) -> None:
    """Start loading data from iris.edu.
    Usage: cli.py load_iris --port=18000 --host=rtserve.iris.washington.edu --channel YN/SGBS2 --channel XL/MG04 --channel WY/YGC
    """
    if len(channel) == 0:
        raise ValueError('There must be at least one channel')
    channels = []
    for raw_channel in channel:
        parsed_channel = raw_channel.split('/')
        if len(parsed_channel) != 2:
            raise ValueError(f'Channel {raw_channel} is not valid. The format [network]/[station]')
        channels.append(Channel(network=parsed_channel[0], station=parsed_channel[1]))
        
    client = IrisClient(host, str(port), channels)
    client.run()


    