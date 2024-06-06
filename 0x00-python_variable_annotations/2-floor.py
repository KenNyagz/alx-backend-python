#!/usr/bin/env python3
'''type-annotated function which takes a float as argument
   and returns the floor of the float'''
import math


def floor(n: float) -> int:
    '''returns a 'floored' float'''
    return math.floor(n)
