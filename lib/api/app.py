from aiohttp import web

from lib.api.routes.external import EXTERNAL_ROUTES

class GeoscopeApplication(web.Application):
    _urls = [
        EXTERNAL_ROUTES,
    ]

    def __init__(self):
        super().__init__(
            middlewares=(),
        )
        self.add_routes()

    def add_routes(self) -> None:
        for routes in self._urls:
            self.router.add_routes(routes)