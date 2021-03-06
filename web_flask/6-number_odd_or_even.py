#!/usr/bin/python3
'''
task 6 module
'''
from flask import Flask
from flask import render_template
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


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def hello_python(text="is cool"):
    '''
    hello Python <3
    '''
    text_fixed = "Python " + text.replace("_", " ")
    return text_fixed


@app.route('/number/<int:n>', strict_slashes=False)
def hello_int(n):
    '''
    hello int number
    '''
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def hello_int_template(n):
    '''
    hello int number in template
    '''
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def hello_int_odd_or_even(n):
    '''
    hello int number in template
    '''
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
