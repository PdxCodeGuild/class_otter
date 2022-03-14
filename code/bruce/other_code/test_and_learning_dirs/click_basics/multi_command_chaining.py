
import click


@click.group(chain=True)
def cli():
    pass


# Any number of these can be called after multi_command_chaining.py.
# I think the 'chain=True' passed in as argument above allows this.
# I suspect this will work if there is some command specified for multi_command_chaining.py.
# Example:
    # <command to call multi_command_chaining.py> first second
# The command 'first' can be used to call the function 'a_func'.
@cli.command('first')
def a_func():
    click.echo('a_func called')


# The command 'second' can be used to call the function 'b_func'.
@cli.command('second')
def b_func():
    click.echo('b_func called')


if __name__ == '__main__':
    cli()


# # Example ouputs:

# $ python multi_command_chaining.py first second
# a_func called
# b_func called

# $ python multi_command_chaining.py second first
# b_func called
# a_func called