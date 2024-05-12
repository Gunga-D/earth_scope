from lib.interactions import InteractionClients
from lib.cache import Cache

class BaseAction(object):
    def __init__(self):
        super().__init__()
        self._clients = InteractionClients()
        self._cache = Cache()
    
    def set_context(self, redis):
        self._redis = redis