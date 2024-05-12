import time
from datetime import datetime, timezone, timedelta
from typing import Callable, List
from abc import ABC, abstractmethod
from dataclasses import dataclass
from obspy.core import Stream

from lib.interactions.entities import GeoserviceStream

@dataclass
class LoadedStream:
    network: str
    station: str
    channel: str

class IndirectClient(ABC):
    @abstractmethod
    def timeseries(self, network: str, station: str, start_time: str, end_time: str) -> Stream:
        pass

    @abstractmethod
    def networks(self) -> List[str]:
        pass

    @abstractmethod
    def stations(self, network: str) -> List[str]:
        pass

class IndirectService(object):
    def __init__(self, client: IndirectClient, data_callback: Callable):
        self.client = client
        self.channels = []
        self.data_callback = data_callback

        self.delay = 300
    
    def select_stream(self, network: str, station: str, channel: str):
        self.channels.append(LoadedStream(network, station, channel))
    
    def get_streams(self) -> List[GeoserviceStream]:
        res = []
        for network in self.client.networks():
            for station in self.client.stations(network):
                res.append(GeoserviceStream(network, station))
        return res

    def run(self):
        last_times = {}
        for channel in self.channels:
            last_times[channel.network + '/' + channel.station] = datetime.now(timezone.utc) - timedelta(minutes=60)

        while True:
            for channel in self.channels:
                current_time = datetime.now(timezone.utc)
                try:
                    stream = self.client.timeseries(channel.network,
                                                    channel.station,
                                                    last_times[channel.network + '/' + channel.station].strftime('%Y-%m-%dT%H:%M:%S'),
                                                    current_time.strftime('%Y-%m-%dT%H:%M:%S')
                                                    )
                    self.data_callback(stream)

                    last_times[channel.network + '/' + channel.station] = datetime.now(timezone.utc) - timedelta(seconds=10)
                except Exception:
                    pass
            time.sleep(self.delay)