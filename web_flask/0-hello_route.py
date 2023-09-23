#!/usr/bin/python3
"""
This script starts a Flask web application.

The web application listens on 0.0.0.0 and port 5000.
It defines a single route: '/' which displays "Hello HBNB!".
The route definition uses the option strict_slashes=False.
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route that displays "Hello HBNB!" when accessed.
    """
    return "Hello HBNB!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
