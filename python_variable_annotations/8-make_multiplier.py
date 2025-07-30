#!/usr/bin/env python3
"""
A function that takes a float and returns a
function that multiplies a float
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Args:
        multiplier (float): The value that the returned function will use
            to multiply its input.

    Returns:
        Callable[[float], float]: A function that takes a float as input
            and returns that float multiplied by the original multiplier.
            The returned function has the signature: (float) -> float

    Examples:
        Create a doubler function:
        >>> double = make_multiplier(2.0)
        >>> double(5.0)
        10.0
        >>> double(3.5)
        7.0

        Create a tripler function:
        >>> triple = make_multiplier(3.0)
        >>> triple(4.0)
        12.0

        Create a function that multiplies by pi:
        >>> pi_multiplier = make_multiplier(3.14159)
        >>> pi_multiplier(2.0)
        6.28318

        Works with negative multipliers too:
        >>> negate = make_multiplier(-1.0)
        >>> negate(5.0)
        -5.0"""
    def inner_function(x: float) -> float:
        return x * multiplier
    return inner_function
