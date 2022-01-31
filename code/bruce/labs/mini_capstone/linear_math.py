# ******************************** #
#   Command Line Easy Calculator   #
#      click pipenv cli math       #
#           Version: 1.0           #
#       Author: Bruce Stull        #
#            2022-01-28            #
# ******************************** #

# Inspiration:
# https://www.symbolab.com/solver/linear-equation-calculator/simplify%20y%20%3D%20-1%5Cleft(x%20-%201%5Cright)%20%2B%201?or=input

import click
from sympy import symbols, solve


@click.group()
# @click.option('-s', '--specform',
#     type=str,
#     default='ps',
#     prompt='What form of input arguments',
#     help='"ps", "si", "pp" form of coefficients.')
def the_linear_maths():
    pass


specform_dict = {
    'ps': 'point-slope',
    'si': 'slope-intercept',
    'pp': 'point-point',
}


# Prompt for three variables to create a linear equation.
# Maybe use option to specify type of equation.
# We are just using the point-slope form for now.
# One of several options:
    # point-slope
    # slope-intercept
    # point-point
@the_linear_maths.command()
@click.option('-x1', '--x1',
    type=float,
    prompt='x-coord',
    help='x-coordinate of the point.')
@click.option('-y1', '--y1',
    type=float,
    prompt='y-coord',
    help='y-coordinate of the point.')
@click.option('-m', '--slope',
    type=float,
    prompt='slope',
    help='Slope of the line, typically written "m".')
@click.option('-x', '--xvalue',
    type=float,
    prompt='xvalue',
    help='x value of the statement.')
def linear_ps(x1, y1, slope, xvalue):
    """Prints point-slope form of linear equation."""
    # tuple_of_symbols = symbols('x1,y,m,x')
    # x1,y,m,x = tuple_of_symbols
    # TODO: Create an option so that linear_ps displays the general
        # form of the equation.
    # TODO: Add return (in addition to calculation) of y value.
    # point-slope: y - y1 = m * (x - x1)
    # click.echo(f'{specform_dict[specform]} chosen.')
    y = 0
    x = xvalue
    y = slope * (x - x1) + y1
    click.echo(f'Linear equation: y = {slope} * (x - {x1}) + {y1}')
    click.echo(f"Your values: x:{x}, y:{y}")


# Solve [0 = m * (x - x1) + y1 - y] for x: (m*x1 + y - y1)/m
# Solve [0 = m * (x - x1) + y1 - y] for y: m*x - m*x1 + y1
# Solve [0 = m * (x - x1) + y1 - y] for m: (y - y1)/(x - x1)
# Solve [0 = m * (x - x1) + y1 - y] for x1: (m*x - y + y1)/m
# Solve [0 = m * (x - x1) + y1 - y] for y1: -m*x + m*x1 + y



# @click.option('-i', '--intercept')

the_linear_maths.add_command(linear_ps)

if __name__ == '__main__':
    the_linear_maths()