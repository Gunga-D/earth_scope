from aiohttp import web
import yaml
from redis import Redis

from lib.api.app import GeoscopeApplication

async def init_app() -> web.Application:
    try:
        with open('./etc/main.config.yml', 'r') as file:
            config = yaml.safe_load(file)
    except FileNotFoundError:
        print(f'ERROR: config file not found')
        return
    
    redis = Redis(
        host=config['redis']['host'],
        port=int(config['redis']['port']),
        password=config['redis']['password'],
        username=config['redis']['username'],
        db=0
    )
    app = GeoscopeApplication(redis)
    return app