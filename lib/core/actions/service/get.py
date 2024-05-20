from lib.core.actions.base import BaseAction
from lib.core.entities.service import Service
from lib.core.preprocesser import SERVICES
from typing import List

class GetServicesAction(BaseAction):
    def __init__(self):
        super().__init__()

    async def handle(self) -> List[Service]:
        return SERVICES