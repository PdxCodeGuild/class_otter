# *********************** #
#          Click          #
#     click pipenv cli    #
#       Version: 1.0      #
#   Author: Bruce Stull   #
#        2022-01-28       #
# *********************** #

import click

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for _ in range(count):
        click.echo(f"Hello, {name}!")

if __name__ == '__main__':
    hello()

########################################################
# If the package is installed, only the 'command' (with any 'options')
# is needed to be typed in CLI:

# 'hello'
# 'hello --name <NAME> --count <COUNT>'

# Since we didn't 'install' this module, these are some commands which
# run the python file and allow passing of options into the function:

# This will prompt for NAME, and use default COUNT:
# 'python hello.py'

# This will use the provided NAME and COUNT values:
# 'python hello.py --count 3 --name Ashton'

# This will use the provided NAME and default COUNT:
# 'python hello.py --name Ashton'