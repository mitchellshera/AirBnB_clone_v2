#!/usr/bin/python3
"""
This script starts a Flask web application.

The web application listens on 0.0.0.0 and port 5000.
It defines four routes:
1. '/' which displays "Hello HBNB!".
2. '/hbnb' which displays "HBNB".
3. '/c/<text>' which displays "C " followed by the value of the text variable
   (replace underscore _ symbols with a space).
4. '/python/<text>' which displays "Python " followed by the value of the text variable
   (replace underscore _ symbols with a space). The default value of text is "is cool".
All route definitions use the option strict_slashes=False.
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays 'HBNB'."""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Displays 'C' followed by the value of <text>.
    Replaces any underscores in <text> with slashes.
    """
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """Displays 'Python' followed by the value of <text>.
    Replaces any underscores in <text> with slashes.
    """
    text = text.replace("_", " ")
    return "Python {}".format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
