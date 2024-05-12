from lib.interactions.ipgp import IPGPClient
from lib.interactions.iris import IrisClient
from lib.interactions.geofon import GeofonClient
from lib.interactions.norsar import NORSARClient
from lib.interactions.bgr import BGRClient
from lib.interactions.usgs import USGSClient
from lib.interactions.usp import USPClient

class InteractionClients(object):
    geoservices = {
        'GEOFON': GeofonClient,
        "IRIS": IrisClient,
        "IPGP": IPGPClient,
        "NORSAR": NORSARClient,
        "BGR": BGRClient,
        "USGS": USGSClient,
        "USP": USPClient
    }