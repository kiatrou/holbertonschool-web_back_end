#!/usr/bin/env python3
"""
Module containing async_comprehension function that collects random numbers
from an async generator using async comprehension syntax.
"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collect 10 random numbers from async_generator using async comprehension.

    This coroutine uses an async comprehension to collect all 10 random numbers
    that are yielded by the async_generator function.
    Since async_generator waits
    1 second between each yield, this function will take
    approximately 10 seconds to complete.

    Returns:
        List[float]: A list containing 10 random floating-point
        numbers between 0 and 10

    Example:
        >>> numbers = await async_comprehension()
        >>> print(numbers)
        [3.45, 7.12, 1.89, 9.23, 0.56, 5.43, 8.90, 2.34, 6.67, 4.12]
        >>> len(numbers)
        10

    Note:
        This function demonstrates async comprehension syntax,
        which is similar to regular list comprehensions but
        works with async iterators using the
        'async for' pattern within the comprehension.
    """
    numbers = [item async for item in async_generator()]
    return numbers
