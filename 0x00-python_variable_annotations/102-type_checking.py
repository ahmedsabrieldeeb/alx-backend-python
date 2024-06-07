#!/usr/bin/env python3
"""
Type checking
"""
from typing import Tuple, Sequence, List, Any


def zoom_array(lst: Sequence[Any], factor: int = 2) -> list:
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


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
