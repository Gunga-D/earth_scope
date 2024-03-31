import click
from typing import List, Optional
from obspy.core import Trace, Stream
from typing import Callable
import os
import datetime
from os.path import normpath
from threading import Lock

from lib.interactions.entities import Channel

def stream_handler(service_name: str, saving_path: str, lock: Optional[Lock] = None):
    def save(channel_info: Channel, stream: Stream, fetched_interval: str) -> Callable:
        pathExists = os.path.exists(saving_path)
        if not pathExists:
            os.makedirs(saving_path)
        
        full_path = normpath(saving_path + '/' + 
                             f'{channel_info.network}-{channel_info.station}|{fetched_interval}.mseed')
        
        if lock is not None:
            lock.acquire()
        try:
            stream.write(full_path, 'MSEED')
        except Exception as e:
            click.echo(f'ERROR: {service_name} cannot saved trace from {channel_info.network}/{channel_info.station} cause {str(e)}')
            return
        finally:
            if lock is not None:
                lock.release()
        click.echo(f'INFO: {service_name} saved {full_path}')

    return save

def trace_handler(service_name: str, saving_path: str, lock: Optional[Lock] = None) -> Callable:
    def save(trace: Trace):
        pathExists = os.path.exists(saving_path)
        if not pathExists:
            os.makedirs(saving_path)
        
        now = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%S')
        full_path = normpath(saving_path + '/' + 
                             f'{trace.stats.network}-{trace.stats.station}|{now}.mseed')
        
        if lock is not None:
            lock.acquire()
        try:
            trace.write(full_path, 'MSEED')
        except Exception as e:
            click.echo(f'ERROR: {service_name} cannot saved trace from {trace.stats.network}/{trace.stats.station} cause {str(e)}')
            return
        finally:
            if lock is not None:
                lock.release()
        click.echo(f'INFO: {service_name} saved {full_path}')

    return save

def fetch_channels(raw_channels: List[str]) -> List[Channel]:
    if raw_channels is None:
        raise ValueError('channels must be filled')
    if len(raw_channels) == 0:
        raise ValueError('there must be at least one channel')
    channels = []
    for raw_channel in raw_channels:
        parsed_channel = raw_channel.split('/')
        if len(parsed_channel) != 2:
            raise ValueError(f'channel {raw_channel} is not valid. The format [network]/[station]')
        channels.append(Channel(network=parsed_channel[0], station=parsed_channel[1]))
    return channels