from lib.core.actions.stream.get import GetStreamsAction
from lib.api.handlers.base import BaseHandler
from lib.api.schemas.stream import (
    GetStreamsResponseSchema
)
from lib.api.exceptions import APIException

class StreamHandler(BaseHandler):
    async def get(self):
        """
        Получить стрим с определенной геофизической службы, стрим - Сеть/Название станции.
        """
        try:
            station = self.get_query_param('service_name')
            streams = await self.run_action(GetStreamsAction, station)
            return self.make_response(GetStreamsResponseSchema(), {'data': streams})
        except APIException as ex:
            return ex.throw()