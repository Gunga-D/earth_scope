import asyncio
from typing import Optional, Callable
from lib.interactions.ipgp.client import HTTPIPGPClient

class Service(object):
    def __init__(self, client: HTTPIPGPClient):
        self.client = client
    
    async def run(self, delay: float, data_callback: Optional[Callable] = None):
        while True:
            stream = self.client.timeseries()
            data_callback(stream)
            await asyncio.sleep(delay)