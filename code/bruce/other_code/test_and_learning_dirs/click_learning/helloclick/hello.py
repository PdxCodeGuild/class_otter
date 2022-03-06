
import click

# Use PassClass object to pass info to commands lower in nest.
# We will:
    # Create the helper class:
        # class PassClass(object)
    # Create helper object:
        # my_pass_object = click.make_pass_decorator(PassClass, ensure=True)
    # Add the decorator '@', '@my_pass_object' immediately before the associated function:
        # @my_pass_object
    # Set values to a variable of the my_pass_variable object while using whatever logic:
        # my_pass_variable.verbose = <value passed to config object>
        # my_pass_variable.home_directory = <value passed to config object>
    # Retreive some values, these can be printed or passed to other logic:
        # my_pass_variable.verbose
        # my_pass_variable.home_directory


# Create helper class.
class PassClass(object):

    def __init__(self):
        self.verbose = False


# Create the pass object.
my_pass_object = click.make_pass_decorator(PassClass, ensure=True)


# Use decorator. This will make a group 'cli' which can group the nested commands.
@click.group()
# Add some options for the group. Options are optional.
@click.option('-v', '--verbose', is_flag=True)
@click.option('-hd', '--home-directory', type=click.Path())
# Declare the pass object to be used.
@my_pass_object
# Define the function. Include the pass variable in the arguments.
def cli(my_pass_variable, verbose, home_directory):
    # Assign some values ot the contents of pass object.
    my_pass_variable.verbose = verbose
    if home_directory is None:
        home_directory = '.'
    my_pass_variable.home_directory = home_directory
    # if verbose:
    #     click.echo(f"Verbose: {verbose}")
    # else:
    #     click.echo(f"Verbose: {verbose}")


# Use decorator. This will add a command 'say' to the 'cli' group.
@cli.command()
# Add some options. Options are optional.
@click.option('-n', '--name',
    default='World',
    type=str,
    help="Specify the name.")
@click.option('-r', '--repeat',
    default=1,
    type=int,
    help="Number of times to be greeted.")
# No 'help' option available for 'argument'.
# Typically, the 'argument' is specified in docstring.
# Add an argument. Arguments are REQUIRED.
@click.argument('out',
    default='-',
    type=click.File('w'),
    required=False)
# Declare the pass object to be used.
@my_pass_object
# Define the function. Include the pass variable in the arguments.
def say(my_pass_variable, name, repeat, out):
    """Greet the user NAME, REPEAT times."""
    # Access the pass variable.
    if my_pass_variable.verbose:
        click.echo(f"my_pass_variable.verbose: {my_pass_variable.verbose}")
    click.echo(f"Home directory: {my_pass_variable.home_directory}")
    click.echo(out)
    for _ in range(repeat):
        # This line writes to the file using .write(), which is not a 'click' function.
        # 'file=out' writes the string to OUT.
        click.echo(f"Greetings, {name}!", file=out)

if __name__ == '__main__':
    cli()