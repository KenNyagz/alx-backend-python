#!/usr/bin/env python3
'''

'''
import asyncio
import random
wait_n = __import__('1-concurrent_coroutines').wait_n
import time
from typing import List


async def measure_time(n: int, max_delay: int) -> float:
    ''' '''
    start = time.perf_counter()
    await wait_n(n, max_delay)
    end = time.perf_counter

    tot_time = end - start
    return tot_time / n
