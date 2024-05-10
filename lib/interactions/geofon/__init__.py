from typing import List, Optional, Callable
from obspy.clients.seedlink.easyseedlink import EasySeedLinkClient
from obspy.core.trace import Trace

class GeofonClient(EasySeedLinkClient):
    def __init__(self, host: str, port: str, data_callback: Optional[Callable] = None):
        super().__init__(host + ':' + port)
        
        self.data_callback = data_callback
        if not self.data_callback:
            self.data_callback = self.default_data_callback

    def default_data_callback(self, trace: Trace):
        print(f'Received geofon trace:\n{trace}\n')

    def on_data(self, trace: Trace):
        self.data_callback(trace)