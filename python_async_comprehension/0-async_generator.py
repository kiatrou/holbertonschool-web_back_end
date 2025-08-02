#!/usr/bin/env python3
"""
Module containing an async generator that yields random numbers with delays.
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Async generator that yields 10 random numbers between 0 and 10.

    This coroutine loops 10 times, waiting 1 second between each iteration,
    then yields a random floating-point number between 0 and 10 (inclusive).

    Yields:
        float: Random number between 0 and 10

    Example:
        >>> async for number in async_generator():
        ...     print(f"Got: {number}")
        Got: 3.45
        Got: 7.12
        ... (continues for 10 numbers total, 1 second apart)

    Note:
        This generator will take approximately 10 seconds to complete
        since it waits 1 second before yielding each number.
    """
    for i in range(10):
        await asyncio.sleep(1)
        number = random.uniform(0, 10)
        yield number
