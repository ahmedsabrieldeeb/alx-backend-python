#!/usr/bin/env python3
"""
safe_first_element module
"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    This function takes a sequence and returns its first element.

    Args:
        lst (Sequence[Any]): a sequence

    Returns:
        Union[Any, NoneType]: the first element of the sequence
                              or None if the sequence is empty
    """
    if lst:
        return lst[0]
    else:
        return None


print(safe_first_element.__annotations__)
