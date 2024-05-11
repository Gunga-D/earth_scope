import click
from rq import Queue, Worker, Connection

@click.command()
def run_worker():
    """Starts queue worker.
    Usage: cli.py run-worker
    """

    with Connection():
        q = Queue()
        Worker(q).work()