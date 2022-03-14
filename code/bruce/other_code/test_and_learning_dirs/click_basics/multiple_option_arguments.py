

import click


@click.command()
@click.option( '-w', '--word',multiple=True)
def words(word):
    click.echo('\n'.join(word))


@click.command()
@click.option('-n', '--number',
    multiple=True,
    type=int,
    )
def add(number):
    for element in number:
        click.echo(f"{type(element)} : {element}")
    click.echo(sum(number))



if __name__ == '__main__':
    # words()
    add()
