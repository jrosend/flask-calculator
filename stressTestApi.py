#!/bin/env python

import requests
import random
import aiohttp
import asyncio


requestsNum = 1000

operations = ['sum', 'subtract', 'multiply', 'divide']

requestsList = [
    f'http://127.0.0.1:8001/{operations[random.randint(0, len(operations)-1)]}/{random.randint(0, 1000)}/{random.randint(0, 1000)}'
    for _ in range(requestsNum)
]

async def stressTest():
    async with aiohttp.ClientSession() as session:
        for request in requestsList:
            async with session.get(request) as resp:
                response = await resp.json()
                print(response)

asyncio.run(stressTest())
