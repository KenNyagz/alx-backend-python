#!/usr/bin/env python3
'''type-annotated function that takes a string and an
 int Or float as arguments and returns a tuple'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''returns a tuple of string k and  number v'''
    return (k, float(v ** 2))
