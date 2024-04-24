from lib.interactions.fdsn import FDSNClient

class IPGPClient(FDSNClient):
    def __init__(self, base_url: str = 'http://ws.ipgp.fr/fdsnws'):
        super().__init__(base_url)


