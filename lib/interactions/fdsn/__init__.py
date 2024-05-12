from lib.interactions.base import IndirectClient
from obspy.core import Stream
from obspy import read
import urllib.request
import io
from typing import List
from xml.dom.minidom import parseString

from lib.config import VERSION
from lib.interactions.fdsn.const import SUPPORTED_SERVICES
from lib.interactions.fdsn.exception import FDSNClientException, FDSNClientNoDataException, FDSNClientInvalidParamsException

class FDSNClient(IndirectClient):
    def __init__(self, base: str):
        if base in SUPPORTED_SERVICES:
            self.base_url = SUPPORTED_SERVICES[base]
        else:
            self.base_url = base
        self.req_opener = urllib.request.build_opener()

    def timeseries(self, network: str, station: str, start_time: str, end_time: str) -> Stream:
        headers = {'User-Agent': f"GeoScopeCLI/{VERSION}"}

        remoteaddr = self.base_url + \
            f'/dataselect/1/query?starttime={start_time}&endtime={end_time}&network={network}&station={station}&format=miniseed'
        
        try:
            req = urllib.request.Request(url=remoteaddr, headers=headers)
            response = self.req_opener.open(req, timeout=10)
        except urllib.request.HTTPError as e:
            raise FDSNClientException(str(e))
        if response.getcode() == 204:
            raise FDSNClientNoDataException()

        data = io.BytesIO(response.read())
        data.seek(0, 0)
        stream = read(data, 'MSEED')
        data.close()
        return stream
    
    def networks(self) -> List[str]:
        headers = {'User-Agent': f"GeoScopeCLI/{VERSION}"}

        remoteaddr = self.base_url + f'/station/1/query?format=xml&level=network'
        try:
            req = urllib.request.Request(url=remoteaddr, headers=headers)
            response = self.req_opener.open(req, timeout=10)
        except urllib.request.HTTPError as e:
            raise FDSNClientException(str(e))
        if response.getcode() == 204:
            raise FDSNClientNoDataException()
        
        res = []
        doc = parseString(response.read())
        networks = doc.getElementsByTagName('Network')
        for network in networks:
            res.append(network.getAttribute('code'))
        return res
        
    def stations(self, network: str) -> str:
        headers = {'User-Agent': f"GeoScopeCLI/{VERSION}"}
        remoteaddr = self.base_url + f'/station/1/query?format=xml&level=station&network={network}'
        try:
            req = urllib.request.Request(url=remoteaddr, headers=headers)
            response = self.req_opener.open(req, timeout=10)
        except urllib.request.HTTPError as e:
            raise FDSNClientException(str(e))
        if response.getcode() == 204:
            raise FDSNClientNoDataException()
        res = []
        doc = parseString(response.read())
        networks = doc.getElementsByTagName('Station')
        for network in networks:
            res.append(network.getAttribute('code'))
        return res
        
