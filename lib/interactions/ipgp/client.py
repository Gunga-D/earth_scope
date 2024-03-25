from lib.interactions.entities import Channel
from obspy.core import Stream
from obspy import read
import urllib.request

from lib.config import settings
from lib.interactions.ipgp.exception import IPGPClientException

class HTTPIPGPClient(object):
    def __init__(self, base_url: str = 'http://ws.ipgp.fr/fdsnws'):
        self.base_url = base_url

    def timeseries(self, channel: Channel, start_time: str, end_time: str) -> Stream:
        headers = {'User-Agent': f'EarthScope/{settings['version']}'}

        remoteaddr = self.base_url + \
            f'/dataselect/1/query?starttime={start_time}&endtime={end_time}&network={channel.network}&station={channel.station}'
        
        req = urllib.request.Request(url=remoteaddr, headers=headers)
        try:
            response = urllib.request.urlopen(req, timeout=5)
        except urllib.request.HTTPError as e:
            raise IPGPClientException(str(e))
        
        data = response.read()
        try: 
            stream = read(data, 'MSEED')
        except Exception:
            raise IPGPClientException('not valid format of response')
        return stream


