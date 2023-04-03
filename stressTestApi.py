#!/bin/env python

import random
import asyncio
import time
import time
import logging
import argparse

from aiohttp import ClientSession

logLevels = {
    'info': logging.INFO,
    'debug': logging.DEBUG,
    'error': logging.ERROR,
    'warning': logging.WARNING
}

parser = argparse.ArgumentParser(description='flask-calc stress test options', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-c', '--context', help='Context to make requests to', default='dev', choices=['dev', 'prod'])
parser.add_argument('-b', '--batches', help='Number of request batches to send', type=int, default=100)
parser.add_argument('-s', '--batch-size', help='Number of request per batch', type=int, default=50)
parser.add_argument('-l', '--log-level', help='Log level to output', type=str, choices=logLevels.keys(), default='info')

config = vars(parser.parse_args())

log = logging.getLogger()
log.addHandler(logging.StreamHandler())
log.setLevel(logLevels[config['log_level']])
#log.basicConfig(format='%(asctime)s %(message)s')


domain=f'flask-calc.{config["context"]}'

requestBatchCount = config['batches']
requestsCount = config['batch_size']

log.info(f'Sending {requestBatchCount} batches of {requestsCount} requests each to {domain}')

operations = ['sum', 'subtract', 'multiply', 'divide']

async def stressTest(requests):
    async with ClientSession() as session:
        for request in requestsList:
            async with session.get(request) as resp:
                response = await resp.json()
                log.debug(response)

startTotalTime = time.time()
for i in range(0, requestBatchCount):
    requestsList = [
        f'http://{domain}/{operations[random.randint(0, len(operations)-1)]}/{random.randint(0, 1000)}/{random.randint(0, 1000)}'
        for _ in range(requestsCount)
    ]
    log.info(f'{i+1}/{requestBatchCount}: Sending {len(requestsList)} requests...')
    start_time = time.time()
    asyncio.run(stressTest(requestsList))
    seconds = time.time() - start_time
    log.info(f'\tFinished in: {time.strftime("%H:%M:%S",time.gmtime(seconds))}')
totalSeconds = time.time() - startTotalTime
log.info(f'Test finished in {time.strftime("%H:%M:%S", time.gmtime(totalSeconds))}')
