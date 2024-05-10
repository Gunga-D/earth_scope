from lib.interactions.fdsn import FDSNClient
from lib.interactions.base import Looper
from lib.interactions.entities import Channel

from typing import List, Callable, Optional

class IPGPClient(Looper):
    def __init__(self, base_url, channels: List[Channel], data_callback: Optional[Callable] = None):
        self.httpclient = FDSNClient(base_url)
        super().__init__(channels, self.httpclient, data_callback)