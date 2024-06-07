#!/usr/bin/env python3
"""
make_multiplier module
"""
from typing import Callable


def make_multiplier(multiplir: float) -> Callable[[float], float]:
    """
    This function takes a float as argument and returns a function that
    takes a float as argument
    and returns the product of the argument of the two functions.

    Args:
        multiplir (float): float to multiply

    Returns:
        Callable[[float], float]: function that does the action
    """
    def multiply(x: float) -> float:
        return x * multiplir

    return multiply
