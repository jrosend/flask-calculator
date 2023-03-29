#!/bin/env python

import random
import asyncio
import time
import time
import logging as log

from aiohttp import ClientSession

log.basicConfig(format='%(asctime)s %(message)s')


requestBatchCount = 20
requestsCount = 500

print(f'Sending {requestBatchCount} batches of {requestsCount} requests each')

operations = ['sum', 'subtract', 'multiply', 'divide']

async def stressTest(requests):
    async with ClientSession() as session:
        for request in requestsList:
            async with session.get(request) as resp:
                response = await resp.json()
                log.debug(response)


for i in range(0, requestBatchCount):
    requestsList = [
        f'http://127.0.0.1:8001/{operations[random.randint(0, len(operations)-1)]}/{random.randint(0, 1000)}/{random.randint(0, 1000)}'
        for _ in range(requestsCount)
    ]
    print(f'{i+1}/{requestBatchCount}: Sending {len(requestsList)} requests...')
    start_time = time.time()
    asyncio.run(stressTest(requestsList))
    seconds = time.time() - start_time
    print('\tFinished in:', time.strftime("%H:%M:%S",time.gmtime(seconds)))
