#!/usr/bin/env python3
'''
Duck type annotation for function taking in a dictionary-like object
'''
from typing import Mapping, Any, Union, TypeVar


T = TypeVar('T')
def safely_get_value(dct: Mapping, key: Any, default: Union[T, None]  = None) -> Union[Any, T]:
    ''' return dictionary key or something else'''
    if key in dct:
        return dct[key]
    else:
        return default
