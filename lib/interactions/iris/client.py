from datetime import datetime
from typing import List, Optional, Callable
from obspy.clients.seedlink.easyseedlink import EasySeedLinkClient
from obspy.core.trace import Trace

from lib.utils.logger import get_product_logger

from lib.interactions.iris.exception import IrisClientException
from lib.interactions.entities import Channel

class IrisClient(EasySeedLinkClient):
    def __init__(self, host: str, port: str, channels: List[Channel], data_callback: Optional[Callable] = None):
        super().__init__(host + ':' + port)

        if len(channels) > 5:
            raise IrisClientException('The service iris edu limit the max concurrent connections, no more than 5')
        if len(channels) == 0:
            raise IrisClientException('At least one channel is required to connect the iris edu service')
        
        self.data_callback = data_callback
        if not self.data_callback:
            self.data_callback = self.default_data_callback
            
        for channel in channels:
            super().select_stream(channel.network, channel.station, '???')

    def default_data_callback(self, trace: Trace):
        logger = get_product_logger()
        logger.info(f'Received iris edu trace from logger:\n{trace}\n')

    def on_data(self, trace: Trace):
        self.data_callback(trace)