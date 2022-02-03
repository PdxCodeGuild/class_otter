# ******************************** #
#   Command Line Easy Calculator   #
#      click pipenv cli math       #
#           Version: 1.0           #
#       Author: Bruce Stull        #
#            2022-01-28            #
# ******************************** #

import click
import math

@click.group()
def the_maths():
    pass


# add() version 1.0
@click.command()
@click.option('-n1', '--number_01',
    type=float,
    prompt='First number',
    help='The first number in addition process.')
@click.option('-n2', '--number_02',
    type=float,
    prompt='Second number',
    help='The second number in addition process.')
@click.option('-p', '--precision',
    type=int,
    default=3,
    # prompt='Level of precision',
    help='The number of decimal digits to round the result by.')
def add(number_01, number_02, precision):
    '''Adds N1 and N2. Returns the value of N1 + N2.'''
    click.echo(f"""{number_01} + {number_02} = {round(
        number_01 + number_02, precision)}""")

# # TODO: Figure out if we can add an arbitrary amount of numbers.
# # How to use *args and **kwargs with 'click'.
# @click.command()


@click.command()
@click.option('-n1', '--number_01',
    type=float,
    prompt='First number',
    help='The first number in subtraction process.')
@click.option('-n2', '--number_02',
    type=float,
    prompt='Second number',
    help='The second number in subtraction process.')
@click.option('-p', '--precision',
    type=int,
    default=3,
    # prompt='Level of precision',
    help='The number of decimal digits to round the result by.')
def subtract(number_01, number_02, precision):
    '''Subtracts N2 from N1. Returns the value of N1 - N2.'''
    click.echo(f"""{number_01} - {number_02} = {round(
        number_01 - number_02, precision)}""")

@click.command()
@click.option('-n1', '--number_01',
    # Default value is shown when displaying the input prompt.
    # The default value also specifies a 'type'.
    type=float,
    prompt='First number',
    help='The first number in multiplication operation.')
@click.option('-n2', '--number_02',
    type=float,
    prompt='Second number',
    help='The second number in multiplication operation.')
@click.option('-p', '--precision',
    type=int,
    default=3,
    # prompt='Level of precision',
    help='The number of decimal digits to round the result by.')
def multiply(number_01, number_02, precision):
    '''Multiplies N1 and N2. Returns the product (multiplication) of
        arguments N1 and N2, with the answer rounded to PRECISION digits.'''
    # Don't seem to need error handling, here, for non numeric.
    # # Error: Invalid value for '-n1', '--number_01': 'a' is not a valid integer.
    click.echo(f"""{number_01} * {number_02} = {round(
        number_01 * number_02, precision)}""")

# TODO: Decide if I want to use 'dividend' instead of 'n1', and similar with 'n2'.
@click.command()
@click.option('-n1', '--number_01',
    type=float,
    prompt='First number',
    help='The first number (dividend/numerator) in division operation.')
@click.option('-n2', '--number_02',
    type=float,
    prompt='Second number',
    help='The second number (divisor/denominator) in division operation.')
@click.option('-p', '--precision',
    type=int,
    default=3,
    # prompt='Level of precision',
    help='The number of decimal digits to round the result by.')
def divide(number_01, number_02, precision):
    '''Divides N1 by N2. Returns the result of division of the two
        arguments N1 and N2, with the answer rounded to PRECISION digits.'''
    if number_02 != 0:
        click.echo(f"""{number_01} / {number_02} = {round(
            number_01 / number_02, precision)}""")
    else:
        click.echo('Sorry, division by zero is not allowed in this realm.')
        # TODO: Display a resource to division by zero.


@click.command()
@click.option('-n', '--number',
    type=int,
    prompt='Number to calculator factorial of',
    help='The number to process I!.')
@click.option('-p', '--precision',
    type=int,
    default=3,
    help='Desired precision of the answer.')
def factorial(number, precision):
    '''Calculate the factorial of NUMBER.'''
    click.echo(f"{number}! = {round(factorial_n(number), precision)}")

def factorial_n(number):
    if number == 0:
        return 1
    return number * factorial_n(number-1)


@click.command()
@click.option('-n', '--number',
    type=float,
    prompt='Number to be the denominator',
    help='The number in the bottom of the fraction.')
@click.option('-p', '--precision',
    type=int,
    default=3,
    help='Desired precision of the answer.')
def inverse(number, precision):
    '''Calculate the inverse of NUMBER.'''
    if number == 0:
        click.echo(f'Invalid input: Input number cannot be {number}')
    click.echo(round(1 / number, precision))


@click.command()
@click.option('-n', '--number',
    type=float,
    prompt='Radicand',
    help='Number inside the square root (radicand)')
@click.option('-p', '--precision',
    type=int,
    default=3,
    help='Desired precision of the answer.')
def sqroot(number, precision):
    '''Calculate the square root of NUMBER with PRECISION decimal places.'''
    click.echo(f'square_root({number}) = {round(math.sqrt(number), precision)}')


@click.command()
@click.option('-n', '--number',
    type=float,
    prompt='Base number',
    help='The base number to be raised to nth power.')
@click.option('-pow', '--power',
    type=float,
    prompt='Power',
    help='The nth powerwhich the base number is being raised to.')
@click.option('-p', '--precision',
    type=int,
    default=3,
    help='Desired precision of the answer.')
def nth_power(number, power, precision):
    """Calculate NUMBER to POWER, with PRECISION decimal places."""
    click.echo(f"{number} ** {power} = {round(number ** power, precision)}")


@click.command()
@click.option('-n', '--number',
    type=float,
    prompt='Argument',
    help='NUMBER to calculate log of.')
@click.option('-b', '--base',
    type=float,
    prompt='Base',
    help='BASE of the log to calculate.')
@click.option('-p', '--precision',
    type=int,
    default=3,
    help='Desired precision of the answer.')
def log(number, base, precision):
    """Calculate log of NUMBER with base BASE."""
    if number <= 0:
        click.echo('Sadly, only non-zero non-negative numbers allowed in this realm.')
    else:
        click.echo(f'log base {base} of {number} = {round(math.log(number, base), precision)}')

# In lieu of using 'the_maths.add_command(<command>)' here,
# we could use a decorator '@the_maths.command()' at each function above.
# See 'trig_math.py' for '@the_trig_maths.command()'.
the_maths.add_command(add)
the_maths.add_command(subtract)
the_maths.add_command(multiply)
the_maths.add_command(divide)
the_maths.add_command(factorial)
the_maths.add_command(inverse)
the_maths.add_command(sqroot)
the_maths.add_command(nth_power)
the_maths.add_command(log)


# Do we need this when using package?
# It would seem it's only needed when we want to run this specific python file. 'python <file_name>.py'.
if __name__ == '__main__':
    the_maths()

