from aiohttp import web

from lib.api.handlers.file import FileHandler
from lib.api.handlers.ping import PingHandler

UTILITY_ROUTES = (
    web.view("/ping", PingHandler),
    web.view('/file/{file_path}', FileHandler)
)