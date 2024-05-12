from typing import List, Optional, Callable
from obspy.clients.seedlink.easyseedlink import EasySeedLinkClient
from obspy.core.trace import Trace
from obspy.core.stream import Stream
from xml.dom.minidom import parseString

from lib.interactions.entities import GeoserviceStream

class USPClient(EasySeedLinkClient):
    def __init__(self,
                data_callback: Optional[Callable] = None):
        super().__init__('seisrequest.iag.usp.br:18000')

        self.data_callback = data_callback
        if not self.data_callback:
            self.data_callback = self.default_data_callback

    def default_data_callback(self, stream: Stream):
        print(f'Received USP trace from logger:\n{stream}\n')

    def on_data(self, trace: Trace):
        self.data_callback(Stream(traces=[trace]))

    def get_streams(self) -> List[GeoserviceStream]:
        raw_data = self.get_info('STREAMS')

        res = []
        doc = parseString(raw_data)
        stations = doc.getElementsByTagName('station')
        for station in stations:
            res.append(GeoserviceStream(network=station.getAttribute('network'), station=station.getAttribute('name')))
        return res