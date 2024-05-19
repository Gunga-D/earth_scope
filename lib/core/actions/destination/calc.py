from lib.core.actions.base import BaseAction
from lib.core.entities.destination import Destination
from lib.core.exceptions import CoreNotFoundError
from lib.core.const import NOT_SUPPORTED_DIST_SERVICES

from geopy.distance import geodesic

class CalcDestinationAction(BaseAction):
    def __init__(self, service_name, network, station, source_latitude, source_longitude):
        self.service_name = service_name
        self.network = network
        self.station = station
        self.source_latitude = source_latitude
        self.source_longitude = source_longitude

        super().__init__()

    async def handle(self) -> Destination:
        if not self.service_name in self._clients.geoservices or \
            self.service_name in NOT_SUPPORTED_DIST_SERVICES:
            raise CoreNotFoundError
        client = self._clients.geoservices[self.service_name]()
        station_info = client.station(self.network, self.station)
        dist = geodesic((self.source_latitude, self.source_longitude), (station_info.latitude, station_info.longitude))

        on_map = f'https://yandex.ru/map-widget/v1/?ll={self.source_longitude}%2C{self.source_latitude}&pt={self.source_longitude}%2C{self.source_latitude}~{station_info.longitude}%2C{station_info.latitude}&rl={self.source_longitude}%2C{self.source_latitude}~{station_info.longitude}%2C{station_info.latitude}&z=2'
        return Destination(kilometers=dist.km, degrees=dist.km/111, on_map=on_map)