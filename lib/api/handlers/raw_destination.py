from lib.api.schemas.raw_destination import (
    CalcRawDestinationRequestSchema,
    CalcRawDestinationResponseSchema,
)
from lib.api.handlers.base import BaseHandler
from lib.api.exceptions import APIException
from lib.core.actions.raw_destination.calc import CalcRawDestinationAction

class CalcRawDestinationHandler(BaseHandler):
    async def post(self):
        """
        Расчет дистанции между выбранными точками.
        """
        try:
            data = await self.get_json_data(CalcRawDestinationRequestSchema())
            res = await self.run_action(CalcRawDestinationAction, **data)
            return self.make_response(CalcRawDestinationResponseSchema(),
                                       {'data': res})
        except APIException as ex:
            return ex.throw()