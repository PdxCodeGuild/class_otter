# ******************************** #
#   Command Line Easy Calculator   #
#      click pipenv cli math       #
#           Version: 1.0           #
#       Author: Bruce Stull        #
#            2022-01-28            #
# ******************************** #

import click

@click.group()
def the_trig_maths():
    pass

@click.command()
@click.option('--rad',
    type=float,
    prompt='Argument value in radians: ',
    help='The number which we are calculating the sin of.')
@click.option('--precision',
    type=int,
    prompt='Level of precision: ',
    help='The number of decimal digits to round the result by.')
def sin(rad, precision):
    '''Accepts two arguments. Returns the value of sin(N), rounded to PRECISION digits.'''
    result = rad - ()/()
    click.echo(f"")


the_trig_maths.add_command(sin)


if __name__ == '__main__':
    the_trig_maths()