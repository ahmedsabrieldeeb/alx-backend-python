#!/usr/bin/env python3
"""
This module contains the function sum_list
that returns the sum of a list of floats and ints
"""
from typing import List, Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    This function returns the sum of a list of floats and ints

    Args:
        input_list: List[int, float]

    Returns:
        The sum of the list
    """
    return (k, v*v)
