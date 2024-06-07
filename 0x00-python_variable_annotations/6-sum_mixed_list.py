#!/usr/bin/env python3
"""
This module contains the function sum_list
that returns the sum of a list of floats and ints
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    This function returns the sum of a list of floats and ints

    Args:
        input_list: List[int, float]

    Returns:
        The sum of the list
    """
    return sum(mxd_lst)
