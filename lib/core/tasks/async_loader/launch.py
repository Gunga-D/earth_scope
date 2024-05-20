from threading import Thread
import time
from obspy.core import Stream
import os
import datetime
import base64
import matplotlib

from lib.core.entities.async_loader import LoadedData
from lib.core.tasks.base import BaseTask
from lib.core.exceptions import CoreNotFoundError
from lib.config import SAVING_PATH

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
        self.saving_path = SAVING_PATH

        super().__init__()

    def handle(self) -> LoadedData:
        if not self.service_name in self._clients.geoservices:
            raise CoreNotFoundError
        
        streams = []
        def save(stream: Stream):
            pathExists = os.path.exists(self.saving_path)
            if not pathExists:
                os.makedirs(self.saving_path)
                
            streams.append(stream)

        client = self._clients.geoservices[self.service_name](data_callback=save)
        client.select_stream(self.network, self.station, 'BH?')
        thread = Thread(target=client.run,daemon=True)
        thread.start()

        timeout = time.time() + self.interval
        while True:
            if time.time() > timeout:
                break
        
        merged_stream = Stream()
        for stream in streams:
            merged_stream += stream
        matplotlib.use('agg')
        raw_data = merged_stream.plot(format='png', show=False, block=False)
        generated_waveform = base64.b64encode(raw_data).decode('utf-8')
        
        full_path = os.path.normpath(self.saving_path + f'/{self.network}_{self.station}_{datetime.date.today().strftime("%I:%M%p-%B-%d-%Y")}.mseed')
        merged_stream.write(full_path, 'MSEED')
        return LoadedData(file=full_path, waveform_data=generated_waveform, waveform_format='base64(png)')
        