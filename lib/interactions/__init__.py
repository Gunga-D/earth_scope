from lib.interactions.ipgp.client import HTTPIPGPClient
from lib.interactions.iris.client import WSIrisClient

class InteractionClients(object):
    ipgp: HTTPIPGPClient
    iris: WSIrisClient