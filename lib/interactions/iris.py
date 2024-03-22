from obspy.clients.seedlink.easyseedlink import EasySeedLinkClient

class MyClient(EasySeedLinkClient):
    def __init__(self, host: str, port: str):
        super().__init__(host + ':' + port)
        
    def on_data(self, trace):
        print('Received trace:')
        print(trace)