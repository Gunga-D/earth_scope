from lib.core.actions.service.get import GetServicesAction
from lib.api.handlers.base import BaseHandler
from lib.api.schemas.service import GetServicesResponseSchema
from lib.api.exceptions import APIException

class ServiceHandler(BaseHandler):
    async def get(self):
        """
        Получить все доступные геослужбы, которые поддерживает данный сервис.
        """
        try:
            services = await self.run_action(GetServicesAction)
            return self.make_response(GetServicesResponseSchema(), {'data': services})
        except APIException as ex:
            return ex.throw()