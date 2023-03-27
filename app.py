#!/bin/env python

from flask import Flask
import logging as log

log.basicConfig(format='%(asctime)s %(clientip)-15s %(user)-8s %(message)s')

app=Flask(__name__)

@app.get('/sum/<int:a>/<int:b>')
def sum(a, b):
    log.info(f'{a} + {b}')
    return {'result': a + b}, 200

@app.get('/subtract/<int:a>/<int:b>')
def subtract(a, b):
    log.info(f'{a} / {b}')
    return {'result': a - b}, 200

@app.get('/multiply/<int:a>/<int:b>')
def multiply(a, b):
    log.info(f'{a} * {b}')
    return {'result': a * b}, 200

@app.get('/divide/<int:a>/<int:b>')
def divide(a, b):
    log.info(f'{a} / {b}')
    if b == 0:
        log.error('Can\'t divide by 0')
        return {'error': 'Can\'t divide by 0'}, 400
    return {'result': a / b}, 200

@app.get('/health')
def health():
    return {'status':'up'}, 200

if __name__ == "__main__":
    app.run(debug=True)