#!/usr/bin/python3
"""
This script starts a Flask web application.

The web application listens on 0.0.0.0 and port 5000.
It defines three routes:
1. '/' which displays "Hello HBNB!".
2. '/hbnb' which displays "HBNB".
3. '/c/<text>' which displays "C " followed by the value of the text variable
   (replace underscore _ symbols with a space).
All route definitions use the option strict_slashes=False.
"""

from flask import Flask
from flask import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route that displays "Hello HBNB!" when accessed.
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Route that displays "HBNB" when accessed.
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """
    Route that displays "C " followed by the value of the text variable
    (replace underscore _ symbols with a space).
    """
    return "C {}".format(escape(text).replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
