from threading import Thread
import time
from obspy.core import Trace
import os
import uuid

from lib.core.tasks.base import BaseTask
from lib.core.exceptions import CoreNotFoundError
from typing import List

class LaunchTask(BaseTask):
    def __init__(self,
                service_name : str,
                network : str,
                station : str,
                interval_sec : int
                ):
        self.service_name = service_name
        self.network = network
        self.station = station
        self.interval = interval_sec
        self.saving_path = './data'

        super().__init__()

    def handle(self) -> List[str]:
        if not self.service_name in self._clients.geoservices:
            raise CoreNotFoundError
        
        saved = []
        def save(trace: Trace):
            pathExists = os.path.exists(self.saving_path)
            if not pathExists:
                os.makedirs(self.saving_path)
        
            full_path = os.path.normpath(self.saving_path + f'/{str(uuid.uuid4())}.mseed')
            print(full_path)
            saved.append(full_path)
            trace.write(full_path, 'MSEED')

        client = self._clients.geoservices[self.service_name](data_callback=save)
        client.select_stream(self.network, self.station, '???')
        thread = Thread(target=client.run,daemon=True)
        thread.start()

        timeout = time.time() + self.interval
        while True:
            if time.time() > timeout:
                break
        return saved
        