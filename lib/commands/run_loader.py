import click
import yaml
import time
from threading import Thread, Lock

from lib.commands import trace_handler, stream_handler
from lib.commands import fetch_channels
from lib.config import SAVING_PATH

from lib.interactions.iris import IrisClient
from lib.interactions.ipgp import IPGPClient
from lib.interactions.geofon import GeofonClient

from lib.services.ipgp import IPGPService

@click.option('--config_path', default='./etc/main.config.yml', help='Path of config', type=(click.STRING))
@click.command()
def run_loader(config_path) -> None:
    """Run loader from all resources.
    Usage: cli.py run_loader --config_path=./etc/main.config.yml
    """
    try:
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
    except FileNotFoundError:
        click.echo(f'ERROR: config file on path - {config_path} not found')
        return
    
    saving_path = SAVING_PATH
    try:
       saving_path =  config['saving_path']
    except KeyError:
        click.echo(f"WARNING: on config doesn't find the tag 'saving_path', so current saving path is '{saving_path}'")

    lock = Lock()
    services = {}
    try:
        services['iris'] = IrisClient(config['iris']['host'], str(config['iris']['port']),
                            fetch_channels(config['iris']['channels']),
                            trace_handler('iris', saving_path, lock))
    except Exception as e:
        if type(e) is KeyError:
            click.echo(f'WARNGING: iris edu is disabled cause config is invalid')
        else:
            click.echo(f'WARNGING: iris edu is disabled cause init throw error: {e}')

    try:
        client = IPGPClient(config['ipgp']['url'])
        services['ipgp'] = IPGPService(fetch_channels(config['ipgp']['channels']),
                                        client, stream_handler('ipgp', saving_path, lock))
    except Exception as e:
        if type(e) is KeyError:
            click.echo(f'WARNGING: ipgp is disabled cause no channels in config')
        else:
            click.echo(f'WARNGING: ipgp is disabled cause fetching channels throw error: {e}')

    try:
        services['geofon'] = GeofonClient(config['geofon']['host'], str(config['geofon']['port']),
                            fetch_channels(config['geofon']['channels']),
                            trace_handler('geofon', saving_path, lock))
    except Exception as e:
        if type(e) is KeyError:
            click.echo(f'WARNGING: geofon is disabled cause config is invalid')
        else:
            click.echo(f'WARNGING: geofon is disabled cause init throw error: {e}')
    

    for name, service in services.items():
        thread = Thread(target=service.run,daemon=True)
        try:
            thread.start()
        except (KeyboardInterrupt, SystemExit):
            click.echo('Received keyboard interrupt, quitting threads.')
        click.echo(f'INFO: {name} has been started')   
    
    try:
        while True:
            time.sleep(100)
    except (KeyboardInterrupt, SystemExit):
        click.echo('INFO: closed the programm')

    