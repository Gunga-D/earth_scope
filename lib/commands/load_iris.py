import click

@click.command()
@click.option('--port', default=18000, help='Seedlink порт для подгрузки данных', type=(click.INT))
@click.option('--host', default='rtserve.iris.washington.edu', help='Seedlink хост для подгрузки данных', type=(click.STRING))
def load_iris(port, host):
    """Запустить загрузку данных из iris.edu.
    Использование: cli.py load_iris --port=18000 --host=rtserve.iris.washington.edu
    """

    