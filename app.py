#!/bin/env python

from flask import Flask

app=Flask(__name__)

@app.get('/sum/<int:a>/<int:b>')
def sum(a, b):
    return {'result': a + b}, 200

@app.get('/subtract/<int:a>/<int:b>')
def subtract(a, b):
    return {'result': a - b}, 200

@app.get('/multiply/<int:a>/<int:b>')
def multiply(a, b):
    return {'result': a * b}, 200

@app.get('/divide/<int:a>/<int:b>')
def divide(a, b):
    return {'result': a / b}, 200

@app.get('/health')
def health():
    return {'status':'up'}, 200

if __name__ == "__main__":
    app.run(debug=True)