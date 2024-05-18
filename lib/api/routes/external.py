from aiohttp import web

from lib.api.handlers.service import ServiceHandler
from lib.api.handlers.stream import StreamHandler
from lib.api.handlers.async_loader import AsyncLoaderHandler
from lib.api.handlers.sync_loader import SyncLoaderHandler
from lib.api.handlers.destination import CalcDestinationHandler

EXTERNAL_ROUTES = [
    web.view("/api/v1/services", ServiceHandler),
    web.view("/api/v1/streams", StreamHandler),
    web.view('/api/v1/async_loader', AsyncLoaderHandler),
    web.view('/api/v1/sync_loader', SyncLoaderHandler),
    web.view('/api/v1/destination', CalcDestinationHandler)
]