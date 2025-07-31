#!/usr/bin/env python3
"""

"""
from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n, max_delay) -> List[float]:
    # Create n tasks (coroutines) but don't run them yet
    tasks = [task_wait_random(max_delay) for _ in range(n)]

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
