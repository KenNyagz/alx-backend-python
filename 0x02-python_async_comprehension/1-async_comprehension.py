#!/usr/bin/env python3
'''
 Async Comprehensions
'''
import asyncio
import random
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[int]:
    '''  Async Comprehensions'''
    random_nos = [no async for no in async_generator()]
    return random_nos
