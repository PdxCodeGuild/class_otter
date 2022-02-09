# ******************************** #
#   Command Line Easy Calculator   #
#      click pipenv cli math       #
#           Version: 1.0           #
#       Author: Bruce Stull        #
#            2022-01-28            #
# ******************************** #

import numpy as np
import click

@click.group()
def the_trig_maths():
    pass

# TODO: Figure out how to use Click to prompt user for r/d first, then proceed with appropriate prompts.
@click.command()
@click.option('-u', '--units',
    prompt='Units of [r]adians or [d]egrees: ',
    help='Specify units of radians or degrees.')
@click.option('-r', '--radians',
    default=0,
    type=float,
    prompt='Argument value in radians: ',
    help='The number which we are calculating the sine of.')
@click.option('-d', '--degrees',
    default=0,
    type=float,
    prompt='Argument value in degrees: ',
    help='The number which we are calculating the sine of.')
@click.option('-p', '--precision',
    type=int,
    prompt='Level of precision: ',
    help='The number of decimal digits to round the result by.')
def sine(units, radians, degrees, precision):
    '''Accepts two arguments. Returns the value of sin(RADIANS), rounded to PRECISION digits.'''
    if units =='r':
        result = round(np.sin(radians), precision)
    elif units == 'd':
        result = round(np.sin(degrees / 180 * np.pi), precision)
    else:
        click.echo("Something isn't working properly.")
        
    # click.echo(f"Radians: sin({radians}) = {round(result, precision)}")
    click.echo(f"Degrees: sin({radians}) = {round(result, precision)}")


the_trig_maths.add_command(sine)


if __name__ == '__main__':
    the_trig_maths()