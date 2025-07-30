#!/usr/bin/env python3
"""
function that takes a string and an int or float
as arguments and returns a tuple.
"""
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Args:
        k (str): The key string to include in the returned tuple
        v (Union[int, float]): The numeric value to be squared. Can be either
            an integer or a float.

    Returns:
        Tuple[str, float]: A tuple containing:
            - First element: The original key string k
            - Second element: The square of v as a float

    Examples:
        >>> to_kv("elevation", 4)
        ('elevation', 16.0)
        >>> to_kv("temperature", 3.5)
        ('temperature', 12.25)
        >>> to_kv("count", -2)
        ('count', 4.0)
        >>> to_kv("pi", 3.14159)
        ('pi', 9.869587728099999)
    """
    return (k, v ** 2)
