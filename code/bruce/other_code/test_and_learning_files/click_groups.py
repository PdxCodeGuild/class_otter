
import click


@click.group()
def messages():
  pass


@click.command()
def generic():
    click.echo('Hello there')


@click.command()
def welcome():
    click.echo('Welcome')


messages.add_command(generic)
messages.add_command(welcome)


if __name__ == '__main__':
    messages()