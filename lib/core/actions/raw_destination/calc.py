from lib.core.actions.base import BaseAction
from lib.core.entities.destination import Destination

from geopy.distance import geodesic

class CalcRawDestinationAction(BaseAction):
    def __init__(self, input_latitude, input_longitude, source_latitude, source_longitude):
        self.input_latitude = input_latitude
        self.input_longitude = input_longitude
        self.source_latitude = source_latitude
        self.source_longitude = source_longitude

        super().__init__()

    async def handle(self) -> Destination:
        dist = geodesic((self.source_latitude, self.source_longitude), (self.input_latitude, self.input_longitude))

        on_map = f'https://yandex.ru/map-widget/v1/?ll={self.source_longitude}%2C{self.source_latitude}&pt={self.source_longitude}%2C{self.source_latitude}~{self.input_longitude}%2C{self.input_latitude}&rl={self.source_longitude}%2C{self.source_latitude}~{self.input_longitude}%2C{self.input_latitude}&z=2'
        return Destination(kilometers=dist.km, degrees=dist.km/111, on_map=on_map)