# ***************************** #
#   Command Line Easy Strings   #
#    click pipenv cli string    #
#          Version: 1.0         #
#      Author: Bruce Stull      #
#           2022-01-28          #
# ***************************** #

import click


@click.command()
@click.option('-c', '--count',
    default=1,
    help='Number of greetings.')
@click.option('-n', '--name',
    prompt='Your name',
    help='The person to greet.')
def greeting(count, name):
    """Greets NAME for a total of COUNT times."""
    click.echo("Welcome to Easy CLI Calculator!")
    for _ in range(count):
        click.echo("Hello, %s!" % name)
