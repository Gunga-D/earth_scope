from lib.interactions.entities import Channel

from abc import ABC, abstractmethod
from obspy.core import Stream

class IndirectClient(ABC):
    @abstractmethod
    def timeseries(self, channel: Channel, start_time: str, end_time: str) -> Stream:
        pass