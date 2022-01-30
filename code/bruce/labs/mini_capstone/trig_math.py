# ******************************** #
#   Command Line Easy Calculator   #
#      click pipenv cli math       #
#           Version: 1.0           #
#       Author: Bruce Stull        #
#            2022-01-28            #
# ******************************** #

import numpy as np
import click


# Create helper class.
class PassClass(object):

    def __init__(self):
        self.chosen_units = 'r'


# Create the pass object.
my_pass_object = click.make_pass_decorator(PassClass, ensure=True)


@click.group()
@click.option('-u', '--units',
    prompt='Units of [r]adians or [d]egrees',
    help='Specify units of radians or degrees.')
@my_pass_object
def the_trig_maths(my_pass_thing,units):
    """Trigonometry functions."""
    my_pass_thing.chosen_units = units


# TODO: Figure out how to use Click to prompt user for r/d first, then proceed with appropriate prompts.
@the_trig_maths.command()
# @click.command()
# @click.option('-u', '--units',
#     prompt='Units of [r]adians or [d]egrees',
#     help='Specify units of radians or degrees.')
@click.option('-a', '--angle',
    default=0,
    type=float,
    prompt='Angle value',
    help='The number which we are calculating the sine of.')
# @click.option('-d', '--degrees',
#     default=0,
#     type=float,
#     prompt='Argument value in degrees',
#     help='The number which we are calculating the sine of.')
@click.option('-p', '--precision',
    type=int,
    default=0,
    prompt='Level of precision',
    help='The number of decimal digits to round the result by.')
@my_pass_object
def sine(my_pass_thing, angle, precision):
    '''Calculates the sine. Returns the value of sin(RADIANS), rounded to PRECISION digits.'''
    if my_pass_thing.chosen_units =='r':
        result = round(np.sin(angle), precision)
    elif my_pass_thing.chosen_units == 'd':
        result = round(np.sin(angle / 180 * np.pi), precision)
    else:
        click.echo("Something isn't working properly.")
    click.echo(f"sin({angle} <{my_pass_thing.chosen_units}>) = {round(result, precision)}")


@the_trig_maths.command()
@click.option('-a', '--angle',
    default=0,
    type=float,
    prompt='Angle value',
    help='The number which we are calculating the cosine of.')
@click.option('-p', '--precision',
    type=int,
    default=0,
    prompt='Level of precision',
    help='The number of decimal digits to round the result by.')
@my_pass_object
def cosine(my_pass_thing, angle, precision):
    '''Calculates the cosine. Returns the value of cosin(RADIANS), rounded to PRECISION digits.'''
    if my_pass_thing.chosen_units =='r':
        result = round(np.cos(angle), precision)
    elif my_pass_thing.chosen_units == 'd':
        result = round(np.cos(angle / 180 * np.pi), precision)
    else:
        click.echo("Something isn't working properly.")
    click.echo(f"cosin({angle} <{my_pass_thing.chosen_units}>) = {round(result, precision)}")

the_trig_maths.add_command(sine)
the_trig_maths.add_command(cosine)


if __name__ == '__main__':
    the_trig_maths()