# -*- coding: utf-8 -*-
"""
    :author: Grey Li (李辉)
    :url: http://greyli.com
    :copyright: © 2018 Grey Li
    :license: MIT, see LICENSE for more details.
"""
import click
from flask import Flask

app = Flask(__name__)


# the minimal Flask application
@app.route('/')
def index():
    return "<h1>Hello Flask</h1>"


# bind multiple URL for one view function

@app.route('/hi')
@app.route('/hello')
def say_hello():
    return '<h1>Hello Flask</h1>'


# dynamic route, URL variable default

@app.route('/greet')
@app.route('/greet/<name>')
def greet(name = 'Programmer'):
    return '<h1>Hello, %s!</h1>'%name

# custom flask cli command

@app.cli.command()
def hello():
    click.echo('Hello, Human!')


