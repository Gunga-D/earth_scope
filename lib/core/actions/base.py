from lib.interactions import InteractionClients

class BaseAction(object):
    def __init__(self):
        super().__init__()
        self._clients = InteractionClients()