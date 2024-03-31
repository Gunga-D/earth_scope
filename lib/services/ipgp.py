from typing import List, Callable

from lib.services.loop import Looper
from lib.interactions.entities import Channel 
from lib.interactions.ipgp import IPGPClient

class IPGPService(Looper):
    def __init__(self, channels: List[Channel], client: IPGPClient, data_callback: Callable):
        super().__init__(channels, client, data_callback)