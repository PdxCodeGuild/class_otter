# ******************************** #
#   Command Line Easy Calculator   #
#      click pipenv cli math       #
#           Version: 1.0           #
#       Author: Bruce Stull        #
#            2022-01-28            #
# ******************************** #

from pyexpat.errors import messages
import click

@click.group()
def the_maths():
    pass


# add() version 1.0
@click.command()
@click.option('-n1', '--number_01',
    type=float,
    prompt='First number: ',
    help='The first number in addition process.')
@click.option('-n2', '--number_02',
    type=float,
    prompt='Second number: ',
    help='The second number in addition process.')
@click.option('-p', '--precision',
    type=int,
    prompt='Level of precision: ',
    help='The number of decimal digits to round the result by.')
def add(number_01, number_02, precision):
    '''Accepts three arguments. Returns the value of N1 + N2, with the answer rounded to PRECISION digits.'''
    click.echo(f"{number_01} + {number_02} = {round(number_01 + number_02, precision)}")

# # TODO: Figure out if we can add an arbitrary amount of numbers.
# @click.command()
# # @click.option('-n', '--number',
# #     type=float,
# #     prompt='Number to add: ',
# #     help='The number to add to the sum.')
# @click.option('-n', '--number',
#     type=int,
#     prompt='How many numbers to add: ',
#     help='The quantity of numbers to add.')
# @click.option('-p', '--precision',
#     default=0,
#     type=int,
#     prompt='Level of precision: ',
#     help='The number of decimal digits to round the result by.')
# def add(number, precision):
#     '''Accepts three arguments. Returns the value of N1 + N2, with the answer rounded to PRECISION digits.'''
#     the_sum = 0
#     for _ in range(number):
#         num = int(input("Enter a number: "))
#         the_sum += num
#     click.echo(f'The sum: {round(the_sum, precision)}')

@click.command()
@click.option('-n1', '--number_01',
    type=float,
    prompt='First number: ',
    help='The first number in subtraction process.')
@click.option('-n2', '--number_02',
    type=float,
    prompt='Second number: ',
    help='The second number in subtraction process.')
@click.option('-p', '--precision',
    type=int,
    prompt='Level of precision: ',
    help='The number of decimal digits to round the result by.')
def subtract(number_01, number_02, precision):
    '''Accepts three arguments. Returns the value of first N1 - N2, with the answer rounded to PRECISION digits.'''
    click.echo(f"{number_01} - {number_02} = {round(number_01 - number_02, precision)}")

@click.command()
@click.option('-n1', '--number_01',
    # Default value is shown when displaying the input prompt.
    # The default value also specifies the 'INTEGER' in
    type=float,
    prompt='First number: ',
    help='The first number in multiplication operation.')
@click.option('-n2', '--number_02',
    type=float,
    prompt='Second number: ',
    help='The second number in multiplication operation.')
@click.option('-p', '--precision',
    type=int,
    prompt='Level of precision: ',
    help='The number of decimal digits to round the result by.')
def multiply(number_01, number_02, precision):
    '''Accepts three numeric arguments. Returns the product (multiplication) of arguments N1 and N2, with the answer rounded to PRECISION digits.'''
    # Don't seem to need error handling, here, for non numeric.
    # # Error: Invalid value for '-n1', '--number_01': 'a' is not a valid integer.
    click.echo(f"{number_01} * {number_02} = {round(number_01 * number_02, precision)}")

# TODO: Decide if I want to use 'dividend' instead of 'n1', and similar with 'n2'.
@click.command()
@click.option('-n1', '--number_01',
    type=float,
    prompt='First number: ',
    help='The first number (dividend) in division operation.')
@click.option('-n2', '--number_02',
    type=float,
    prompt='First number: ',
    help='The second number (divisor) in division operation.')
@click.option('-p', '--precision',
    type=int,
    prompt='Level of precision: ',
    help='The number of decimal digits to round the result by.')
def divide(number_01, number_02, precision):
    '''Accepts three numeric arguments. Returns the result of division of the two arguments N1 and N2, with the answer rounded to PRECISION digits.'''
    if number_02 != 0:
        click.echo(f"{number_01} / {number_02} = {round(number_01 / number_02, precision)}")
    else:
        click.echo('Sorry, division by zero is not allowed in this realm.')
        # TODO: Display a resource to division by zero.
    
the_maths.add_command(add)
the_maths.add_command(subtract)
the_maths.add_command(multiply)
the_maths.add_command(divide)


# Do we need this when using package?
# It would seem it's only needed when we want to run this specific python file. 'python <file_name>.py'.
if __name__ == '__main__':
    the_maths()
    # greeting()
    # multiply()
    pass

