import click
from typing import List
from obspy.core import Stream
from os.path import normpath
import asyncio
import os

from lib.interactions.ipgp import IPGPClient
from lib.services.ipgp import IPGPService
from lib.interactions.entities import Channel
from lib.config import SAVING_PATH

@click.command()
@click.option('--url', default='http://ws.ipgp.fr/fdsnws', help='Base url of ipgp client', type=(click.STRING))
@click.option('--channel', default=['G/CCD', 'PF/CAS'], multiple=True, help='Receive channels in format [network]/[station]')
def load_ipgp(url, channel: List[str]) -> None:
    """Start loading data only from ipgp.
    Usage: cli.py load_ipgp --url=http://ws.ipgp.fr/fdsnws --channel G/CCD --channel PF/CAS
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

    def saving(channel_info: Channel, stream: Stream, fetched_interval: str):
        pathExists = os.path.exists(SAVING_PATH)
        if not pathExists:
            os.makedirs(SAVING_PATH)
        
        full_path = normpath(SAVING_PATH + '/' + 
                             f'{channel_info.network}-{channel_info.station}|{fetched_interval}.mseed')
        try:
            stream.write(full_path, 'MSEED')
        except Exception as e:
            click.echo(f'cannot saved trace from {channel_info.network}/{channel_info.station} cause {str(e)}')
            return
        click.echo(f'saved {full_path}')

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(service.run(delay=300, data_callback=saving))