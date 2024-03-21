from typing import Sequence
import click

class CLI(click.Group):
    def __init__(self, commands: Sequence) -> None:
        super().__init__(commands=commands, options_metavar="[ОПЦИИ]", subcommand_metavar="КОМАНДА [АРГУМЕНТЫ]...", help="Помощь", add_help_option=False)
