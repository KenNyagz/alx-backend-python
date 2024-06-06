#!/usr/bin/env python3
'''type-annotated function which takes a list  of floats as argument
   and returns their sum as a float'''
from typing import List
from functools import reduce


def sum_list(input_list: List[float]) -> float:
    '''returns sum of floats'''
    return(reduce(lambda x, y: x + y, input_list))
