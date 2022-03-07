
import click


@click.group()
def messages():
  pass


@click.command()
def generic():
    click.echo('Hello there')


@click.command()
def welcome():
    click.echo('Welcome')


messages.add_command(generic)
messages.add_command(welcome)


if __name__ == '__main__':
    # Adding 'messages()' here, in 'main', allows us to run this file
    # and then access the commands after the statement to run the file
    # 'python click_groups.py'.
        # python click_groups.py generic
    messages()


# # Examples:

# $ python click_groups.py generic
# Hello there

# $ python click_groups.py welcome
# Welcome

# These commands can't be chained together.
# Only one following command allowed.
# Note 'unexpected extra argument (generic)'.
# 'generic' is the 'extra argument'.

# $ python click_groups.py welcome generic
# Usage: click_groups.py welcome [OPTIONS]
# Try 'click_groups.py welcome --help' for help.

# Error: Got unexpected extra argument (generic)