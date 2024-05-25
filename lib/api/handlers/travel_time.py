from lib.api.schemas.travel_time import (
    CalcWaveTravelTimeRequestSchema,
    CalcWaveTravelTimeResponseSchema,
)
from lib.api.handlers.base import BaseHandler
from lib.api.exceptions import APIException
from lib.core.actions.travel_time.calc import CalcTraveTimeAction

class CalcWaveTravelTimeHandler(BaseHandler):
    async def post(self):
        """
        Расчет времени распространения сейсмической волны по заданным параметрам.
        """
        try:
            data = await self.get_json_data(CalcWaveTravelTimeRequestSchema())
            res = await self.run_action(CalcTraveTimeAction, **data)
            return self.make_response(CalcWaveTravelTimeResponseSchema(),
                                       {'data': res})
        except APIException as ex:
            return ex.throw()