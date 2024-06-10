#!/usr/bin/env python3
'''asynchronous coroutine that takes in an integer, max_delay, with a
   default value of 10 that waits for a random delay between 0 and
  `max_delay` (included and float value) seconds and eventually returns it
'''
import random
import asyncio
from typing import Union


async def wait_random(max_delay: int = 10) -> float:
    '''Waits for a random delay btn 0 and max_delay sec and returns delay'''
    delay_time: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay_time)
    return delay_time
