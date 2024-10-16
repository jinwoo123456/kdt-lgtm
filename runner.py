#from urllib import request, parse, error
#import json
import requests
import os
import sys
import click
if __name__ == '__main__':

    @click.command()
    @click.option('--words', default='Hello')
    @click.argument('name')
    def greet(name, words):
        click.echo(f'{words}, {name}!')


    if __name__ == '__main__':
        greet()
        args = sys.argv
        for arg in args:
            print(arg)