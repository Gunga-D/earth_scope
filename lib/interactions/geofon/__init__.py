from typing import List, Optional, Callable
from obspy.clients.seedlink.easyseedlink import EasySeedLinkClient
from obspy.core.trace import Trace

from lib.interactions.entities import Channel
from lib.interactions.geofon.exception import GeofonClientException

class GeofonClient(EasySeedLinkClient):
    def __init__(self, host: str, port: str, channels: List[Channel], data_callback: Optional[Callable] = None):
        super().__init__(host + ':' + port)

        if len(channels) == 0:
            raise GeofonClientException('At least one channel is required to connect the geofon service')
        
        self.data_callback = data_callback
        if not self.data_callback:
            self.data_callback = self.default_data_callback
            
        for channel in channels:
            super().select_stream(channel.network, channel.station, '???')

    def default_data_callback(self, trace: Trace):
        print(f'Received geofon trace:\n{trace}\n')

    def on_data(self, trace: Trace):
        self.data_callback(trace)