from aiohttp import web

from lib.api.handlers.ping import PingHandler

UTILITY_ROUTES = (
    web.view("/ping", PingHandler),
)