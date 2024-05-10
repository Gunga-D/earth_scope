from lib.core.actions.base import BaseAction
from lib.core.entities.stream import Stream
from lib.core.exceptions import CoreNotFoundError

from typing import List
from xml.dom.minidom import parseString

class GetStreamsAction(BaseAction):
    def __init__(self, service_name):
        self.service_name = service_name
        super().__init__()

    async def handle(self) -> List[Stream]:
        if not self.service_name in self._clients.geoservices:
            raise CoreNotFoundError
        client = self._clients.geoservices[self.service_name]('geofon-open.gfz-potsdam.de', '18000')
        raw_data = client.get_info('STREAMS')

        res = []
        doc = parseString(raw_data)
        stations = doc.getElementsByTagName('station')
        for station in stations:
            channels = []
            for channel in station.getElementsByTagName('stream'):
                channels.append(channel.getAttribute('seedname'))
            res.append(Stream(network=station.getAttribute('network'), station=station.getAttribute('name'), channels=channels))
        return res
        