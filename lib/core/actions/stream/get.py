from lib.core.actions.base import BaseAction
from lib.core.entities.stream import Stream
from lib.core.exceptions import CoreNotFoundError

from typing import List
from dataclasses import asdict

class GetStreamsAction(BaseAction):
    def __init__(self, service_name):
        self.service_name = service_name
        super().__init__()
    
    async def handle(self) -> List[Stream]:
        if not self.service_name in self._clients.geoservices:
            raise CoreNotFoundError
        
        self._stream_cache = self._cache.stream()
        self._stream_cache.redis(self._redis)

        streams = self._stream_cache.get_streams(self.service_name)
        if streams is None:
            client = self._clients.geoservices[self.service_name]()
            data = client.get_streams()
            res = []
            for part in data:
                res.append(asdict(Stream(part.network, part.station, [])))
            self._stream_cache.create_streams(self.service_name, res)
            streams = res
        return streams
        