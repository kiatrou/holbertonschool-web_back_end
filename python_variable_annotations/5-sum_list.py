#!/usr/bin/env python3
"""
Function which takes a list of floats and returns their sum as a float
"""


def sum_list(input_list: list[float]) -> float:
    """
    Args:
        input_list list[float]: a list of float numbers

    Returns:
        float: the sum of the float numbers

    Examples:
        >>> sum_list([1.5, 2.3, 4.2])
        8.0
        >>> sum_list([])
        0.0
    """
    return sum(input_list)
