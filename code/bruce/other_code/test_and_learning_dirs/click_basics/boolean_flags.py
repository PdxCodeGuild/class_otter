# Resources:
# https://click.palletsprojects.com/en/8.0.x/options/#boolean-flags

import click

import sys

@click.command()
@click.option('--shout/--no-shout', default=False)
def info(shout):
    rv = sys.platform
    if shout:
        rv = rv.upper() + '!!!!111'
    click.echo(rv)


if __name__ == '__main__':
    info()