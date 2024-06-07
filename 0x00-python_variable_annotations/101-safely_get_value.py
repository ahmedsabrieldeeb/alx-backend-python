#!/usr/bin/env python3
"""
TypeVar Usage
"""
from typing import TypeVar, Mapping, Any, Union


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: T,
                     default: Union[T, None] = None) -> Union[T, Any]:
    """
    Safely get a value from a dictionary.

    Args:
        dct: The dictionary to get the value from.
        key: The key to look up in the dictionary.
        default: The default value to return if key is not in the dictionary.

    Returns:
        The value from the dictionary,
        or the default value if the key is not in the dictionary.
    """
    if key in dct:
        return dct[key]
    else:
        return default
