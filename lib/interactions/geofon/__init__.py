from typing import List, Optional, Callable
from obspy.clients.seedlink.easyseedlink import EasySeedLinkClient
from obspy.core.trace import Trace
from obspy.core.stream import Stream
from xml.dom.minidom import parseString

from lib.interactions.fdsn import FDSNClient
from lib.interactions.entities import LoadedStream, GeoserviceStream, StationInfo, SeedlinkConnectionInfo

class GeofonClient(EasySeedLinkClient):
    def __init__(self,
                 data_callback: Optional[Callable] = None):
        self._seedlink_connection_info = SeedlinkConnectionInfo('geofon-open.gfz-potsdam.de', '18000')

        super().__init__(self._seedlink_connection_info.host + ':' + self._seedlink_connection_info.port)
        self.httpclient = FDSNClient('GEOFON')

        self.channels = []

        self.data_callback = data_callback
        if not self.data_callback:
            self.data_callback = self.default_data_callback

    def default_data_callback(self, stream: Stream):
        print(f'INFO: Received geofon trace:\n{stream}\n')

    def on_data(self, trace: Trace):
        self.data_callback(Stream(traces=[trace]))
    
    def select_stream(self, net, station, selector=None):
        self.channels.append(LoadedStream(net, station, selector))
        super().select_stream(net, station, selector)

    def station(self, net, station) -> StationInfo:
        return self.httpclient.stations(net, station)[0]
    
    def scrap(self, left_time: str, right_time: str):
        res = []
        for channel in self.channels:
            stream = self.httpclient.timeseries(channel.network,
                                                channel.station,
                                                left_time,
                                                right_time
                                                )
            res.append(stream)
        return res

    def get_streams(self) -> List[GeoserviceStream]:
        raw_data = self.get_info('STREAMS')

        res = []
        doc = parseString(raw_data)
        stations = doc.getElementsByTagName('station')
        for station in stations:
            res.append(GeoserviceStream(network=station.getAttribute('network'), station=station.getAttribute('name')))
        return res
    
    def get_connection_info(self) -> SeedlinkConnectionInfo:
        return self._seedlink_connection_info
