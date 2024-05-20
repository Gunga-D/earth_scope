from lib.core.entities.service import Service, Connection
from lib.interactions import InteractionClients
from lib.core.const import NOT_SUPPORTED_SCRAP_SERVICES, NOT_SUPPORTED_DIST_SERVICES

from typing import List

class Services:
    def __init__(self, clients):
        self._services = []
        for name in clients:
            has_supported_scrap = not name in NOT_SUPPORTED_SCRAP_SERVICES
            has_supported_dist = not name in NOT_SUPPORTED_DIST_SERVICES

            conn = clients[name]().get_connection_info()
            self._services.append(Service(name=name,
                                    has_supported_scrap=has_supported_scrap,
                                    has_supported_dist=has_supported_dist,
                                    connection=Connection(conn.host, conn.port)
                        ))
    def get_services(self) -> List[Service]:
        return self._services

SERVICES = Services(InteractionClients().geoservices).get_services()