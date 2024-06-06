#!/usr/bin/env python3
'''
type annotation for a function that takes in a list of sequnces
and returns a list of tuples with a sequence and an int each
'''
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''returns list of tuples with a sequence and the length of it'''
    return [(i, len(i)) for i in lst]
