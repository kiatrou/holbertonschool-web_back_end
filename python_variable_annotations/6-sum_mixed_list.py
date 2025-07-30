#!/usr/bin/env python3
"""
Function that takes a list of integers and floats and returns their sum as a float
"""
from typing import List


def sum_mixed_list(mxd_list: List[int, float]) -> float:
    """
    Args:
        mxd_list List[int, float]: a list of integers and floats

    Returns:
        float: sum of the list

    Examples:
    >>> sum_mixed_list([1.2, 4, 5])
    10.2
    >>> sum_mixed_list([8, 2.5, 3.6, 7])
    21.1
    """
    return sum(mxd_list)