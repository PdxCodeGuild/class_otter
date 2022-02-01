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
import matplotlib.pyplot as plt
import numpy as np


@click.group()
# @click.option('-s', '--specform',
#     type=str,
#     default='ps',
#     prompt='What form of input arguments',
#     help='"ps", "si", "pp" form of coefficients.')
def the_linear_maths():
    pass


# specform_dict = {
#     'ps': 'point-slope',
#     'si': 'slope-intercept',
#     'pp': 'point-point',
# }


# Prompt for three variables to create a linear equation.
# Maybe use option to specify type of equation.
# We are just using the point-slope form for now.
# One of several options:
    # point-slope       : y - y1 = m (x - x1)
    # slope-intercept   : y = m x + b
    # point-point       : y - y1 = (y2 - y1) / (x2 - x1) * (x - x1)
@the_linear_maths.command()
@click.option('-plot', '--do_plot',
    default=False,
    is_flag=True,
    help='Flag for displaying plot using "numpy" and "matplotlib"')
@click.option('-x1', '--x1',
    type=float,
    prompt='x-value',
    help='x-value of the point.')
@click.option('-y1', '--y1',
    type=float,
    prompt='y-value',
    help='y-value of the point.')
@click.option('-m', '--slope',
    type=float,
    prompt='slope',
    help='Slope of the line, typically written "m".')
@click.option('-x', '--xvalue',
    type=float,
    prompt='xvalue',
    help='x value of the statement.')
def linear_ps(x1, y1, slope, xvalue, do_plot):
    """Prints Point-Slope form of linear equation."""
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
    click.echo(f'Point-Slope form: y - {y1} = {slope} * (x - {x1})')
    click.echo(f"Your values: x:{x}, y:{y}")
    if do_plot:
        plot_a_line(slope,x1,y1,x,y)


@the_linear_maths.command()
@click.option('-plot', '--do_plot',
    default=False,
    is_flag=True,
    help='Flag for displaying plot using "numpy" and "matplotlib"')
@click.option('-m', '--slope',
    type=float,
    prompt='slope',
    help='Slope of the line, typically written "m".')
@click.option('-yint', '--yint',
    type=float,
    prompt='y-intercept',
    help='Value of y-intercept.')
@click.option('-x', '--xvalue',
    type=float,
    prompt='xvalue',
    help='x value of the statement.')
def linear_si(slope, yint, xvalue, do_plot):
    """Prints Slope-Intercept form of linear equation."""
    # slope-intercept   : y = m x + b
    x = xvalue
    y = slope * x + yint
    click.echo(f"Slope-Intercept form: y = {slope} * x + {yint}")
    click.echo(f"Your values: x:{x}, y:{y}")
    if do_plot:
        plot_a_line(slope,0,yint,x,y)


@the_linear_maths.command()
@click.option('-plot', '--do_plot',
    default=False,
    is_flag=True,
    help='Flag for displaying plot using "numpy" and "matplotlib"')
@click.option('-x1', '--x1',
    type=float,
    prompt='x-value',
    help='x-value of the first point.')
@click.option('-y1', '--y1',
    type=float,
    prompt='y-value',
    help='y-value of the first point.')
@click.option('-x2', '--x2',
    type=float,
    prompt='x-value',
    help='x-value of the second point.')
@click.option('-y2', '--y2',
    type=float,
    prompt='y-value',
    help='y-value of the second point.')
@click.option('-x', '--xvalue',
    type=float,
    prompt='xvalue',
    help='x value of the statement.')
def linear_pp(x1, y1, x2, y2, xvalue, do_plot):
    """Prints Point-Point form of linear equation."""
    # point-point       : y - y1 = (y2 - y1) / (x2 - x1) * (x - x1)
    x = xvalue
    y = (y2 - y1) / (x2 - x1) * (x - x1) + y1
    click.echo(f"Point-Point form: y - {y1} = ({y2} - {y1}) / ({x2} - {x1}) * (x - {x1})")
    click.echo(f"Your values: x:{x}, y:{y}")
    if do_plot:
        plot_a_line((y2 - y1) / (x2 - x1),x1,y1,x,y)


def plot_a_line(slope, ex, wye, ux, uy):
    '''Plots a line from provided 'slope', and a points' 'x' and 'y' values.
        Also plots a single point from provided 'ux' and uy'.'''
    m = slope
    x1 = ex
    y1 = wye
    line_label = f"{m} * (x - {x1}) + {y1}"

    x = np.linspace(-5, 5, 100)
    y = m * (x - x1) + y1
    fig, ax = plt.subplots()
    # Plot the user-defined point.
    ax.plot(ux, uy, 'go', label=f'User Point: {ux},{uy}')
    # Plot the line from y = m * (x - x1) + y1
    ax.plot(x, y, label=line_label)
    ax.set_aspect('equal')
    # Display the grid.
    ax.grid(True, which='both')

    # Plot the axes.
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')

    # loc= 'best', 'upper right', 'upper left', 'lower left', 'lower right', 'right', 'center left', 'center right', 'lower center', 'upper center', 'center'
    # Display the legend in 'best' position.
    plt.legend(loc='best', shadow=True)
    plt.show()


# NOTE: Maybe provide three groups of inputs and present the linear
    # equation of one type?


# the_linear_maths.add_command(linear_ps)
# the_linear_maths.add_command(linear_si)
# the_linear_maths.add_command(linear_pp)


if __name__ == '__main__':
    the_linear_maths()