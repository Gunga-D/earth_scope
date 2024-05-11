import click
from aiohttp import web
import yaml
from redis import Redis

from lib.api.app import GeoscopeApplication

@click.command()
@click.option('--port', default=8001, help='Port number')
@click.option('--host', default='127.0.0.1', help='Bind address')
@click.option('--config_path', default='./etc/main.config.yml', help='Path of config')
def run_server(port, host, config_path):
    """Starts api web server.
    Usage: cli.py run-server --port=8001 --host=127.0.0.1
    """
    try:
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
    except FileNotFoundError:
        click.echo(f'ERROR: config file on path - {config_path} not found')
        return
    
    redis = Redis(
        host=config['redis']['host'],
        port=int(config['redis']['port']),
        password=config['redis']['password'],
        username=config['redis']['username'],
        db=0
    )
    
    app = GeoscopeApplication(redis)
    web.run_app(app, port=port, host=host)