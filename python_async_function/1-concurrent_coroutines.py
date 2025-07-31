#!/usr/bin/env python3
"""
Spawn wait_random n times with the specified max_delay.
    Returns a list of delays in ascending order without using sort().
"""
import asyncio
import bisect
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    Args:
        n (int): Number of times to call wait_random
        max_delay (int): Maximum delay for each wait_random call

    Returns:
        List[float]: List of delays in ascending order
    """
    # Create n tasks (coroutines) but don't run them yet
    tasks = [wait_random(max_delay) for _ in range(n)]

    # Run all tasks concurrently and get results
    results = await asyncio.gather(*tasks)

    # Insert each result in ascending order without using sort()
    ordered_delays = []
    for delay in results:
        bisect.insort(ordered_delays, delay)

    return ordered_delays
