import click
from pathlib import Path
from collections import deque


@click.command()
@click.option('-n', '--lines', type=click.INT, default=10, help='Number of lines to print.')
@click.argument('file', type=click.File(mode='r'))
def tail(file, lines):
    for line in deque(file, maxlen=lines):
        click.echo(line, nl=False)


if __name__ == '__main__':
    tail()
