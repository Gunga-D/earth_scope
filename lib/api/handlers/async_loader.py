from lib.api.handlers.base import BaseHandler
from lib.api.schemas.async_loader import (
    LaunchAsyncLoaderRequestSchema,
    LaunchAsyncLoaderResponseSchema
)
from lib.core.tasks.async_loader.launch import LaunchTask
from lib.api.exceptions import APIException
from lib.config import HTTP_FILE_URL

class AsyncLoaderHandler(BaseHandler):
    async def get(self):
        """
        Получение информации по запущенной асинхронной задаче.
        """
        try:
            task_id = self.get_query_param('task_id')
            job = self.request.app.queue.fetch_job(task_id)
            data = None
            if job.get_status() == 'finished':
                data = job.return_value()
                data.file = HTTP_FILE_URL + data.file.replace('/', '%2F')
            return self.make_response(LaunchAsyncLoaderResponseSchema(),
                                       {'data': {'task_id': task_id, 'status': job.get_status(), 'result': data}})
        except APIException as ex:
            return ex.throw()

    async def post(self):
        """
        Запустить асинхронную загрузку mseed файлов c определенного стрима.
        """
        try:
            stream = await self.get_json_data(LaunchAsyncLoaderRequestSchema())
            if stream.interval_sec > 15:
                raise APIException(code=400, message='interval must be <= 15 sec')
            
            job = self.enqueue_task(LaunchTask, **stream)
            return self.make_response(LaunchAsyncLoaderResponseSchema(), {'data': {'task_id': job.id}})
        except APIException as ex:
            return ex.throw()