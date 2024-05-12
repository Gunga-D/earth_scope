from aiohttp import web
from typing import Optional
from redis import Redis
from rq import Queue
import aiohttp_cors

from lib.api.routes.external import EXTERNAL_ROUTES
from lib.api.routes.utiliy import UTILITY_ROUTES

class GeoscopeApplication(web.Application):
    _urls = [
        EXTERNAL_ROUTES,
        UTILITY_ROUTES,
    ]

    def __init__(self, redis: Optional[Redis] = None):
        super().__init__(
            middlewares=(),
        )
        if not redis:
            self.redis = redis
        else:
            self.redis = Redis()
        self.queue = Queue(connection=self.redis)

        self.add_routes()

    def add_routes(self) -> None:
        for routes in self._urls:
            self.router.add_routes(routes)
        self._setup_cors()
        
    def _setup_cors(self) -> None:
        cors = aiohttp_cors.setup(self, defaults={
            "*": aiohttp_cors.ResourceOptions(
                allow_credentials=True,
                expose_headers="*",
                allow_headers="*"
            )  
        })
        for route in list(self.router.routes()):
            cors.add(route)