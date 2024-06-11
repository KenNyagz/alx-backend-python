#!/usr/bin/env python3
'''
type hinted coroutine that takes no arguments, loops 10 times waiting for 1 sec
each the yield a custom number
'''
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    ''' oops 10 times waiting for 1 sec each the yield a custom numbe'''
    for i in range(10):
        task = asyncio.create_task(asyncio.sleep(1))
        await task
        yield random.uniform(0, 10)
