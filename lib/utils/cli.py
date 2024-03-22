from typing import Sequence, Optional
import click

class CLI(click.Group):
    def __init__(self, commands: Sequence, help: Optional[str] = None) -> None:
        super().__init__(commands=commands, help=help, add_help_option=False)
