from lib.api.schemas.station_destination import (
    CalcStationDestinationRequestSchema,
    CalcStationDestinationResponseSchema,
)
from lib.api.handlers.base import BaseHandler
from lib.api.exceptions import APIException
from lib.core.actions.station_destination.calc import CalcStationDestinationAction

class CalcStationDestinationHandler(BaseHandler):
    async def post(self):
        """
        Расчет дистанции между выбранной станцией и заданными координатами.
        """
        try:
            data = await self.get_json_data(CalcStationDestinationRequestSchema())
            res = await self.run_action(CalcStationDestinationAction, **data)
            return self.make_response(CalcStationDestinationResponseSchema(),
                                       {'data': res})
        except APIException as ex:
            return ex.throw()