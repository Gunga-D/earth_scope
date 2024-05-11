from aiohttp import web
from marshmallow import Schema, ValidationError

from lib.core.exceptions import (
    CoreBaseExceptionError,
    CoreNotFoundError,
    CoreDataError,
    CoreAlreadyExistsError,
)
from lib.api.exceptions import APIException
from lib.core.actions.base import BaseAction
from lib.core.tasks.base import BaseTask
from rq.job import Job

def raise_api_exception(exc: CoreBaseExceptionError) -> web.Response:
    message = getattr(exc, 'message', 'Internal server error')

    code = 500
    if isinstance(exc, CoreNotFoundError):
        code = 404
    if isinstance(exc, CoreAlreadyExistsError):
        code = 409
    if isinstance(exc, CoreDataError):
        code = 400

    raise APIException(code=code, message=message)

class BaseHandler(web.View):
    async def get_json_data(self, struct: Schema) -> Schema:
        try:
            return struct.load(await self.request.json())
        except ValidationError:
            raise APIException(code=400, message='Invalid request')
    
    def get_path_param(self, path: str) -> str:
        value = self.request.match_info.get(path, None)
        if value is None:
            raise APIException(code=400, message='Invalid request')
        return value
    
    def get_query_param(self, query: str) -> str:
        if not query in self.request.rel_url.query:
            raise APIException(code=400, message='Invalid request')
        return self.request.rel_url.query[query]
    
    def make_response(self, schema: Schema, data: object, status: int = 200):
        return web.Response(headers={'content-type': 'application/json'},
                            text=schema.dumps(data),
                            status = status)
    
    def enqueue_task(self, task: BaseTask, *args, **kwargs) -> Job:
        cls = task(*args, **kwargs)
        return self.request.app.queue.enqueue(cls.handle)

    async def run_action(self, action: BaseAction, *args, **kwargs):
        try:
            return await action(*args, **kwargs).handle()
        except CoreBaseExceptionError as ex:
            raise_api_exception(ex)