#!/usr/bin/env python3
'''
async routine that spawns wait_random(that can a delay a max of max_delay
seconds) n times and return the list of delay
'''
import asyncio
import random
from typing import List
import heapq
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''async routine that spawns wait_random(that can a delay a max
       of max_delay seconds) n times and return the list of delays'''
    asyncs_list = []
    for _ in range(0, n):
        task = asyncio.create_task(wait_random(max_delay))
        asyncs_list.append(task)

    delays: List[float] = await asyncio.gather(*asyncs_list)
    heap: List[float] = []

    for delay in delays:
        heapq.heappush(heap, delay)

    sorted_delays = [heapq.heappop(heap) for _ in range(n)]
    return sorted_delays
