# ***************************** #
#   Command Line Easy Strings   #
#    click pipenv cli string    #
#          Version: 1.0         #
#      Author: Bruce Stull      #
#           2022-01-28          #
# ***************************** #

import click

@click.group()
def bpi():
    pass


@bpi.command()
@click.option('-c', '--count',
    default=1,
    help='Number of greetings.')
@click.option('-n', '--name',
    prompt='Your name',
    help='The person to greet.')
def greeting(count, name):
    """Greets NAME for a total of COUNT times."""
    for _ in range(count):
        click.echo("Hello, %s!" % name)


@bpi.command()
# @click.option('--basic-math')
# @click.option('--trig-math')
# @click.option('--linear-math')
# @click.option('--strings')
# def list_modules(basic_math, trig_math, linear_math, strings):
def list_modules():
    '''Display list of modules.'''
    click.echo("\nWelcome to Easy CLI Calculator!\n")
    click.echo("List of modules:\n")
    modules = ['basic-math', 'trig-math', 'linear-math', 'strings']
    for module in modules:
        click.echo(f"  {module}")


if __name__ == '__main__':
    bpi()