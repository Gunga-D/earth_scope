import click

from lib.commands import stream_handler
from lib.config import SAVING_PATH
from lib.interactions.fdsn import FDSNClient
from lib.interactions.entities import Channel

@click.command()
@click.option('--service', default="IRIS", help='The seismological facility name', type=(click.STRING))
@click.option('--network', default='IU', help='The network code', type=(click.STRING))
@click.option('--station', default='AFI', help='The station code', type=(click.STRING))
@click.option('--left_time', default='', help='The left time of interval, the format is "year"-"month"-"day"T"hour":"minutes":"seconds"', type=(click.STRING))
@click.option('--right_time', default='', help='The right time of interval, the format is "year"-"month"-"day"T"hour":"minutes":"seconds"', type=(click.STRING))
def load_fdsn(service, network, station, left_time, right_time) -> None:
    """Manual load the stream data from fdsn service.
    Usage: cli.py load-fdsn --service=IRIS --network IU --station AFI --left_time=2024-01-18T22:12:10 --right_time=2024-01-18T22:12:30
    """

    client = FDSNClient(service)
    stream = client.timeseries(Channel(network, station), left_time, right_time)
    stream_handler("manual_fdsn_"+service, SAVING_PATH)(Channel(network, station), stream, left_time+"-"+right_time)