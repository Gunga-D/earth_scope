from aiohttp import web
from lib.api.handlers.base import BaseHandler

class PingHandler(BaseHandler):
    async def get(self):
        return web.Response(text='pong')