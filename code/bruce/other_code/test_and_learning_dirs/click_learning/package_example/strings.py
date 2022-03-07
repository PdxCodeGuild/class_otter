# ***************************** #
#   Command Line Easy Strings   #
#    click pipenv cli string    #
#          Version: 1.0         #
#      Author: Bruce Stull      #
#           2022-01-28          #
# ***************************** #

import click


@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
# The '--count' above maps to 'count' below.
# The '--name' above maps to 'name' below.
def greeting(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for _ in range(count):
        # click.echo(f"Hello, {name}!")
        click.echo("Hello, %s!" % name)
