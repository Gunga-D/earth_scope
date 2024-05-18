from lib.api.schemas.destination import (
    CalcDestinationRequestSchema,
    CalcDestinationResponseSchema,
)
from lib.api.handlers.base import BaseHandler
from lib.api.exceptions import APIException
from lib.core.actions.destination.calc import CalcDestinationAction

class CalcDestinationHandler(BaseHandler):
    async def post(self):
        """
        Расчет дистанции между выбранной станцией и заданными координатами.
        """
        try:
            data = await self.get_json_data(CalcDestinationRequestSchema())
            res = await self.run_action(CalcDestinationAction, **data)
            return self.make_response(CalcDestinationResponseSchema(),
                                       {'data': res})
        except APIException as ex:
            return ex.throw()