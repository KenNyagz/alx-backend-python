#!/usr/bin/env python3
'''type-annotated function  which takes a list of integers and
   floats and returns their sum as a float'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''Returns sum of ints or floats as a float'''
    return float(sum(mxd_lst))
