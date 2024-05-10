from lib.interactions.ipgp import IPGPClient
from lib.interactions.iris import IrisClient
from lib.interactions.geofon import GeofonClient

class InteractionClients(object):
    geoservices = {
        'GEOFON': GeofonClient,
        "IRIS": IrisClient,
        "IPGP": IPGPClient,
    }