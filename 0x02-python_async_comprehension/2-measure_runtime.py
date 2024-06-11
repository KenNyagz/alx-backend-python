#!/usr/bin/env python3
'''
Run async function in parallel four times and measure the time taken
'''
import asyncio
import random
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    ''' Measure time taken to run four programs in parallel'''
    start = time.perf_counter()
    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         )
    end = time.perf_counter()
    tot_time = end - start
    return tot_time
