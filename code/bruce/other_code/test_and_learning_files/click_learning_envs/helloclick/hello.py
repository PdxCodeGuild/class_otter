
import click

# Use Config object to pass info to commands lower in nest.
class Config(object):

    def __init__(self):
        self.verbose = False

pass_config = click.make_pass_decorator(Config, ensure=True)


@click.group()
@click.option('-v', '--verbose', is_flag=True)
@click.option('-hd', '--home-directory', type=click.Path())
@pass_config
def cli(config, verbose, home_directory):
    config.verbose = verbose
    if home_directory is None:
        home_directory = '.'
    config.home_directory = home_directory
    # if verbose:
    #     click.echo(f"Verbose: {verbose}")
    # else:
    #     click.echo(f"Verbose: {verbose}")

@cli.command()
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
@click.argument('out',
    default='-',
    type=click.File('w'),
    required=False)
@pass_config
def say(config, name, repeat, out):
    """Greet the user, NAME, REPEAT times."""
    if config.verbose:
        click.echo(f"config.verbose: {config.verbose}")
    click.echo(f"Home directory: {config.home_directory}")
    # This line writes to the file using .write(), which is not a 'click' function.
    click.echo(out)
    for _ in range(repeat):
        # 'file=out' writes the string to OUT.
        click.echo(f"Greetings, {name}!", file=out)