#!/usr/bin/env python3
"""
Function that returns the floor of a float
"""


def floor(n: float) -> int:
    """
    Args:
        n (float): The number to find the floor of
        
    Returns:
        int: The largest integer less than or equal to n
        
    Examples:
        >>> floor(3.7)
        3
        >>> floor(3.0)
        3
        >>> floor(-2.3)
        -3
    """
    if n > 0:
        return int(n)
    else:
        if n == int(n):
            return int(n)
        else:
            return int(n) - 1
