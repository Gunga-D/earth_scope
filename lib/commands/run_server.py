import asyncio
import click
from aiohttp import web

from lib.api.app import GeoscopeApplication

@click.command()
@click.option('--port', default=8001, help='Port number')
@click.option('--host', default='127.0.0.1', help='Bind address')
def run_server(port, host):
    """Starts api web server.
    Usage: cli.py run_server --port=8001 --host=127.0.0.1
    """

    app = GeoscopeApplication()
    web.run_app(app, port=port, host=host)