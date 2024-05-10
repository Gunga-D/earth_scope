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
        
    def make_response(self, schema: Schema, data: object, status: int = 200):
        print(schema.dumps(data))
        return web.Response(headers={'content-type': 'application/json'},
                            text=schema.dumps(data),
                            status = status)
    
    async def run_action(self, action: BaseAction, *args, **kwargs):
        try:
            return await action(*args, **kwargs).handle()
        except CoreBaseExceptionError as ex:
            raise_api_exception(ex)