#!/usr/bin/env python3
"""
This module contains the function sum_list
that returns the sum of a list of floats
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    This function returns the sum of a list of floats

    Args:
        input_list: list[float]

    Returns:
        The sum of the list
    """
    return sum(input_list)
