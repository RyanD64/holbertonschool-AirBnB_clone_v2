#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """return value"""
    return f'Hello HBNB!'


@app.route('/hbnb')
def first():
    """return value"""
    return f'HBNB!'


@app.route('/c/<text>')
def second(text):
    """return value"""
    result = text.replace('_', ' ')
    return f"C {result}"


@app.route('/python')
@app.route('/python/<text>')
def third(text='is cool'):
    """return value"""
    text = text.replace('_', ' ')
    return f"Python {text}"


@app.route('/number/<n>')
def fourth(n):
    """return value"""
    return f"{n} is a number"


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
