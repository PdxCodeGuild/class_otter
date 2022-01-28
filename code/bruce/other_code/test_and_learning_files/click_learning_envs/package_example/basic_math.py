# ******************************** #
#   Command Line Easy Calculator   #
#      click pipenv cli math       #
#           Version: 1.0           #
#       Author: Bruce Stull        #
#            2022-01-28            #
# ******************************** #

# from email.policy import default
import click

@click.command()
@click.option('--n1',
    type=float,
    prompt='First number: ',
    help='The first number in addition process.')
@click.option('--n2',
    type=float,
    prompt='Second number: ',
    help='The second number in addition process.')
@click.option('--precision',
    type=int,
    prompt='Level of precision: ',
    help='The number of decimal digits to round the result by.')
def add(n1, n2, precision):
    '''Accepts two arguments. Returns the value of first N1 + N2.'''
    click.echo(f"{n1} + {n2} = {round(n1 + n2, precision)}")

@click.command()
@click.option('--n1',
    type=float,
    prompt='First number: ',
    help='The first number in subtraction process.')
@click.option('--n2',
    type=float,
    prompt='Second number: ',
    help='The second number in subtraction process.')
@click.option('--precision',
    type=int,
    prompt='Level of precision: ',
    help='The number of decimal digits to round the result by.')
def subtract(n1, n2, precision):
    '''Accepts two arguments. Returns the value of first N1 - N2.'''
    click.echo(f"{n1} - {n2} = {round(n1 - n2, precision)}")

@click.command()
@click.option('--n1',
    # Default value is shown when displaying the input prompt.
    # The default value also specifies the 'INTEGER' in
    type=float,
    prompt='First number: ',
    help='The first number in multiplication operation.')
@click.option('--n2',
    type=float,
    prompt='Second number: ',
    help='The second number in multiplication operation.')
@click.option('--precision',
    type=int,
    prompt='Level of precision: ',
    help='The number of decimal digits to round the result by.')
def multiply(n1, n2, precision):
    '''Accepts two numeric arguments. Returns the product (multiplication) of arguments N1 and N2.'''
    # Don't seem to need error handling, here, for non numeric.
    # # Error: Invalid value for '--n1': 'a' is not a valid integer.
    click.echo(f"{n1} * {n2} = {round(n1 * n2, precision)}")

# TODO: Decide if I want to use 'dividend' instead of 'n1', and similar with 'n2'.
@click.command()
@click.option('--n1',
    type=float,
    prompt='First number: ',
    help='The first number (dividend) in division operation.')
@click.option('--n2',
    type=float,
    prompt='First number: ',
    help='The second number (divisor) in division operation.')
@click.option('--precision',
    type=int,
    prompt='Level of precision: ',
    help='The number of decimal digits to round the result by.')
def divide(n1, n2, precision):
    '''Accepts two numeric arguments. Returns the result of division of the two arguments N1 and N2.'''
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

