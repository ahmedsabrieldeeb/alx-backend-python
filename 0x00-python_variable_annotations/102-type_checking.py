#!/usr/bin/env python3
"""
Type checking
"""
from typing import Tuple, List, Any


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Returns a list that is a zoomed-in version of the input list by 2

    Args:
        lst: Sequence of any type
        factor: int

    Returns:
        List: A list that is a zoomed-in version of the input list by 2
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


print(zoom_array.__annotations__)
