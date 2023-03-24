#!/bin/env python

import requests
import random


requestsNum = 1000

operations = ['sum', 'subtract', 'multiply', 'divide']

for i in range(0, requestsNum):
    operation = operations[random.randint(0, len(operations)-1)]
    randomA = random.randint(0, 1000)
    randomB = random.randint(1, 1000)
    response = requests.get(f'http://127.0.0.1:37783/{operation}/{randomA}/{randomB}')
    print(response.json())