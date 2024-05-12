from lib.interactions.fdsn import FDSNClient
from lib.interactions.base import IndirectService

from typing import Callable, Optional

class NORSARClient(IndirectService):
    def __init__(self,
                data_callback: Optional[Callable] = None):
        self.httpclient = FDSNClient('http://eida.geo.uib.no/fdsnws')
        super().__init__(self.httpclient, data_callback)