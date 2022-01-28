# ******************************* #
#      Click Library Example      #
#   click library decorator cli   #
#           Version: 0.0          #
#       Author: Bruce Stull       #
#            2022-01-27           #
# ******************************* #

import pprint
import requests
import click

@click.command()
def hello():
    click.echo('Hello there')



def main():
    pass

if __name__ == '__main__':
    hello()