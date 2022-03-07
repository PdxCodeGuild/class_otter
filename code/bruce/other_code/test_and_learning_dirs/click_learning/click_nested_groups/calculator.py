
import click

from .math import commands as math
from .trig import commands as trig

@click.group()
def entry_point():
    pass

entry_point.add_command(math.command_group)
entry_point.add_command(trig.version)