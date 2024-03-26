from typing import List

from lib.services.loop import Looper
from lib.interactions.entities import Channel 
from lib.interactions.ipgp import IPGPClient

class IPGPService(Looper):
    def __init__(self, channels: List[Channel], client: IPGPClient):
        super().__init__(channels, client)