#!/usr/bin/env python3
"""
element_length module
"""
from typing import List, Tuple, Sequence


def element_length(lst: List[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    This function takes a list of sequences and returns a list of tuples
    where each tuple contains a sequence and its length.

    Args:
        lst (List[Sequence]): list of sequences

    Returns:
        List[Tuple[Sequence, int]]: list of tuples
    """
    return [(i, len(i)) for i in lst]
