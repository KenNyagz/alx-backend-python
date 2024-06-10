#!/usr/bin/env python3
'''
Measure the runtime of an asynchronous function
'''
import asyncio
import random
import time
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    ''' Measure the runtime of an asynchronous function'''
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()

    tot_time = end - start
    return tot_time / n
