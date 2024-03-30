import click
from typing import List
from obspy.core import Trace
from os.path import normpath
import datetime
import os

from lib.config import SAVING_PATH
from lib.interactions.iris import IrisClient
from lib.interactions.entities import Channel

@click.command()
@click.option('--port', default=18000, help='Seedlink port to load the data', type=(click.INT))
@click.option('--host', default='rtserve.iris.washington.edu', help='Seedlink host to load the data', type=(click.STRING))
@click.option('--channel', default=['YN/SGBS2', 'XL/MG04', 'WY/YGC'], multiple=True, help='Receive channels in format [network]/[station]')
def load_iris(port, host, channel: List[str]) -> None:
    """Start loading data only from iris.edu.
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
    
    def saving(trace: Trace):
        pathExists = os.path.exists(SAVING_PATH)
        if not pathExists:
            os.makedirs(SAVING_PATH)
        
        now = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%S')
        full_path = normpath(SAVING_PATH + '/' + 
                             f'{trace.stats.network}-{trace.stats.station}|{now}.mseed')
        
        try:
            trace.write(full_path, 'MSEED')
        except Exception as e:
            click.echo(f'cannot saved trace from {trace.stats.network}/{trace.stats.station} cause {str(e)}')
            return
        click.echo(f'saved {full_path}')

    client = IrisClient(host, str(port), channels, saving)
    client.run()


    