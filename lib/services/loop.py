import asyncio
import time
from typing import Optional, Callable, List

from lib.interactions.entities import Channel 
from lib.interactions.indirect import IndirectClient

class Looper(object):
    def __init__(self, channels: List[Channel], client: IndirectClient):
        self.client = client
        self.channels = channels
    
    async def run(self, delay: float, data_callback: Optional[Callable] = None):
        last_times = {}
        for channel in self.channels:
            last_times[channel.network + '/' + channel.station] = time.time()
            
        while True:
            for channel in self.channels:
                current_time = time.time()
                stream = self.client.timeseries(channel,
                                                time.strftime('%Y-%m-%dT%H:%M:%S',
                                                            last_times[channel.network + '/' + channel.station]),
                                                time.strftime('%Y-%m-%dT%H:%M:%S',
                                                            current_time))
                last_times[channel.network + '/' + channel.station] = time.time()
                data_callback(stream)
            await asyncio.sleep(delay)