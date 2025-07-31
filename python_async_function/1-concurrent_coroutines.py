#!/usr/bin/env python3
"""
Spawn wait_random n times with the specified max_delay.
    Returns a list of delays in ascending order
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

    # Insert each result in ascending order
    ordered_delays = []
    for delay in results:
        # Find the right position to insert
        inserted = False
        for i in range(len(ordered_delays)):
            if delay < ordered_delays[i]:
                ordered_delays.insert(i, delay)
                inserted = True
                break
        # If not inserted, it belongs at the end
        if not inserted:
            ordered_delays.append(delay)

    return ordered_delays
