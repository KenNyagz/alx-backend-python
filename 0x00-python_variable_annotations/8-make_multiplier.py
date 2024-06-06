#!/usr/bin/env python3
'''type-annotated function that takes a float multiplier
as argument and returns a function that multiplies a float by multiplier'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''makes and returns a function that multiplies a float'''
    def multiply(n: float) -> float:
        return n * multiplier
    return multiply
