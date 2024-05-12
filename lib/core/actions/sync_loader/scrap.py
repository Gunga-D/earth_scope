import os
import uuid
import base64
from dataclasses import asdict

from lib.core.actions.base import BaseAction
from lib.core.entities.sync_loader import ScrapedData
from lib.core.exceptions import CoreNotFoundError
from lib.config import SAVING_PATH

class ScrapAction(BaseAction):
    def __init__(self, service_name, network, station, left_time, right_time):
        self.service_name = service_name
        self.network = network
        self.station = station
        self.left_time = left_time
        self.right_time = right_time
        self.saving_path = SAVING_PATH

        super().__init__()
    
    async def handle(self) -> ScrapedData:
        if not self.service_name in self._clients.geoservices:
            raise CoreNotFoundError

        scrap_cache = self._cache.scrap()
        scrap_cache.redis(self._redis)

        res = scrap_cache.get_scrap(self.service_name, self.network, self.station, self.left_time, self.right_time)
        if res is None:
            client = self._clients.geoservices[self.service_name]()
            client.select_stream(self.network, self.station, '???')
            streams = client.scrap(self.left_time, self.right_time)
            generated_stream = streams[0]

            pathExists = os.path.exists(self.saving_path)
            if not pathExists:
                os.makedirs(self.saving_path)
            full_path = os.path.normpath(self.saving_path + f'/{str(uuid.uuid4())}.mseed')
            generated_stream.write(full_path, 'MSEED')

            raw_data = generated_stream.plot(format='png', show=False, block=False)
            generated_waveform = base64.b64encode(raw_data).decode('utf-8')

            res = asdict(ScrapedData(full_path, generated_waveform, 'base64(png)'))
            scrap_cache.save_scrap(self.service_name, self.network, self.station, self.left_time, self.right_time, res)
        return res