import click

@click.command()
@click.option('--port', default=18000, help='Seedlink port to load the data', type=(click.INT))
@click.option('--host', default='rtserve.iris.washington.edu', help='Seedlink host to load the data', type=(click.STRING))
def load_iris(port, host):
    """Start loading data from iris.edu.
    Usage: cli.py load_iris --port=18000 --host=rtserve.iris.washington.edu
    """

    