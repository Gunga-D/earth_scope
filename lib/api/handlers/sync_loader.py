from lib.api.handlers.base import BaseHandler
from lib.api.schemas.sync_loader import (
    ScrapSyncLoaderRequestSchema,
    ScrapSyncLoaderResponseSchema
)
from lib.core.actions.sync_loader.scrap import ScrapAction
from lib.api.exceptions import APIException
from lib.config import HTTP_FILE_URL


class SyncLoaderHandler(BaseHandler):
    async def post(self):
        """
        Запустить синхронную загрузку mseed файлов c определенного стрима.
        """
        try:
            stream = await self.get_json_data(ScrapSyncLoaderRequestSchema())
            data = await self.run_action(ScrapAction, **stream)
            return self.make_response(ScrapSyncLoaderResponseSchema(), {'data': {'file': HTTP_FILE_URL + data['file'].replace('/', '%2F'),
                                                                                'waveform_data': data['waveform_data'],
                                                                                'waveform_format': data['waveform_format']
                                                                                }})
        except APIException as ex:
            return ex.throw()