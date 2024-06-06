#!/usr/bin/env python3
'''
duck-typed annotation for any input and any output expected from function
'''
from typing import Any, Sequence, Union


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    ''' checks existenct fo sequence'''
    if lst:
        return lst[0]
    else:
        return None
