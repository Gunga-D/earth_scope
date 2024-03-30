import asyncio
from datetime import datetime, timezone, timedelta
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
            last_times[channel.network + '/' + channel.station] = datetime.now(timezone.utc) - timedelta(minutes=60)

        while True:
            for channel in self.channels:
                current_time = datetime.now(timezone.utc)
                try:
                    stream = self.client.timeseries(channel,
                                                last_times[channel.network + '/' + channel.station].strftime('%Y-%m-%dT%H:%M:%S'),
                                                current_time.strftime('%Y-%m-%dT%H:%M:%S'))

                    fetched_interval = f"{last_times[channel.network + '/' + channel.station].strftime('%Y-%m-%dT%H:%M:%S')}-{current_time.strftime('%Y-%m-%dT%H:%M:%S')}"
                    data_callback(channel, stream, fetched_interval)

                    last_times[channel.network + '/' + channel.station] = datetime.now(timezone.utc) - timedelta(seconds=10)
                except Exception:
                    pass
            await asyncio.sleep(delay)