# ******************************** #
#   Command Line Easy Calculator   #
#      click pipenv cli math       #
#           Version: 1.0           #
#       Author: Bruce Stull        #
#            2022-01-28            #
# ******************************** #

from email.policy import default
import click

@click.command()
@click.option('--n1',
    # Default value is shown when displaying the input prompt.
    # The default value also specifies the 'INTEGER' in
    default=3,
    prompt='First number: ',
    help='The first number in multiplication operation.')
@click.option('--n2',
    default=7,
    prompt='Second number: ',
    help='The second number in multiplication operation.')
def multiply(n1,n2):
    '''Accepts two numeric arguments. Returns the product (multiplication) of the two arguments.'''
    # Don't seem to need error handling, here, for non numeric.
    # # Error: Invalid value for '--n1': 'a' is not a valid integer.
    click.echo(f"{n1} * {n2} = {n1 * n2}")

# TODO: Decide if I want to use 'dividend' instead of 'n1', and similar with 'n2'.
@click.command()
@click.option('--n1',
    default=1,
    prompt='First number: ',
    help='The first number (dividend) in division operation.')
@click.option('--n2',
    default=1,
    prompt='First number: ',
    help='The second number (divisor) in division operation.')
@click.option('--precision',
    default=2,
    prompt='Level of precision: ',
    help='The number of decimal digits to round the result by.')
def divide(n1,n2,precision):
    '''Accepts two numeric arguments. Returns the result of division of the two arguments.'''
    if n2 != 0:
        click.echo(f"{n1} / {n2} = {round(n1 / n2, precision)}")
    else:
        click.echo('Sorry, division by zero is not allowed in this realm.')
        # TODO: Display a resource to division by zero.
    

# Do we need this when using package?
# It would seem it's only needed when we want to run this specific python file. 'python <file_name>.py'.
if __name__ == '__main__':
    # greeting()
    # multiply()
    pass

