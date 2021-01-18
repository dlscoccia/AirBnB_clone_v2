#!/usr/bin/python3
'''
task 2 module
'''
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    '''
    hello route
    '''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    '''
    hello HBNB
    '''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def hello_c(text):
    '''
    hello C
    '''
    text_fixed = "C " + text.replace("_", " ")
    return text_fixed


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
