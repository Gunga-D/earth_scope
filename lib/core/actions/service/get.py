from lib.core.actions.base import BaseAction
from lib.core.entities.service import Service

from typing import List

class GetServicesAction(BaseAction):
    def __init__(self):
        super().__init__()

    async def handle(self) -> List[Service]:
        res = []
        for name in self._clients.geoservices:
            res.append(Service(name=name))
        return res