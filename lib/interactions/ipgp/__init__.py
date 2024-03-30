from lib.interactions.indirect import IndirectClient
from lib.interactions.entities import Channel
from obspy.core import Stream
from obspy import read
import urllib.request
import io

from lib.config import VERSION
from lib.interactions.ipgp.exception import IPGPClientException, IPGPCClientNoDataException

class IPGPClient(IndirectClient):
    def __init__(self, base_url: str = 'http://ws.ipgp.fr/fdsnws'):
        self.base_url = base_url
        self.req_opener = urllib.request.build_opener()

    def timeseries(self, channel: Channel, start_time: str, end_time: str) -> Stream:
        headers = {'User-Agent': f"GeoScopeCLI/{VERSION}"}

        remoteaddr = self.base_url + \
            f'/dataselect/1/query?starttime={start_time}&endtime={end_time}&network={channel.network}&station={channel.station}&format=miniseed'
        
        try:
            req = urllib.request.Request(url=remoteaddr, headers=headers)
            response = self.req_opener.open(req, timeout=10)
        except urllib.request.HTTPError as e:
            raise IPGPClientException(str(e))
        if response.getcode() == 204:
            raise IPGPCClientNoDataException()

        data = io.BytesIO(response.read())
        data.seek(0, 0)
        stream = read(data, 'MSEED')
        data.close()
        return stream


