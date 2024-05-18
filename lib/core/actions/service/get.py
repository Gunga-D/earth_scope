from lib.core.actions.base import BaseAction
from lib.core.entities.service import Service

from typing import List
from lib.core.const import NOT_SUPPORTED_SCRAP_SERVICES, NOT_SUPPORTED_DIST_SERVICES

class GetServicesAction(BaseAction):
    def __init__(self):
        super().__init__()

    async def handle(self) -> List[Service]:
        res = []
        for name in self._clients.geoservices:
            has_supported_scrap = not name in NOT_SUPPORTED_SCRAP_SERVICES
            has_supported_dist = not name in NOT_SUPPORTED_DIST_SERVICES
            res.append(Service(name=name, has_supported_scrap=has_supported_scrap, has_supported_dist=has_supported_dist))
        return res