#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/count/<int:parameter>')
def count_route(parameter):
    count_output = '\n'.join(str(i) for i in range(parameter)) + '\n'
    return count_output

@app.route('/print/<parameter>')
def print_route(parameter):
    print(parameter)
    return parameter

@app.route('/math/<int:num1>/<operator>/<int:num2>')
def math_route(num1, operator, num2):
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == 'div':
        result = num1 / num2
    elif operator == '%':
        result = num1 % num2    
    else:
        return "Invalid operator"

    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
    
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

