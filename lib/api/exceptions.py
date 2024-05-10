from aiohttp import web

from lib.api.schemas.base import FailedResponseSchema

class APIException(Exception):
    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message

    def throw(self):
        schema = FailedResponseSchema()
        return web.Response(headers={'content-type': 'application/json'},
                            text=schema.dumps(self),
                            status = self.code)