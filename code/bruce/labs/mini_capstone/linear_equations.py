# ******************************** #
#   Command Line Easy Calculator   #
#      click pipenv cli math       #
#           Version: 1.0           #
#       Author: Bruce Stull        #
#            2022-01-28            #
# ******************************** #

import click


@click.group()
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
@click.command()
@click.option('-s', '--specform',
    type=str,
    default='ps',
    prompt='What form of input arguments',
    help='"ps", "si", "pp" form of coefficients.')
@click.option('-px', '--pointx',
    type=float,
    prompt='x-coord',
    help='x-coordinate of the point.')
@click.option('-py', '--pointy',
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
def linear_ps(specform, pointx, pointy, slope, xvalue):
    """Prints point-slope form of linear equation and returns y value."""
    # TODO: Create an option so that linear_ps displays the general form of the equation.
    click.echo(f'{specform_dict[specform]} chosen.')
    y = 0
    x = xvalue
    y = slope * (x - pointx) + pointy
    click.echo(f'{slope} * (x - {pointx}) + {pointy}')
    click.echo(f"x:{x}, y:{y}")



# @click.option('-i', '--intercept')

the_linear_maths.add_command(linear_ps)

if __name__ == '__main__':
    the_linear_maths()