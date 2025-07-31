#!/usr/bin/env python3
"""
Measures the total execution time for wait_n(n
max_delay) and returns total_time / n.
"""
import asyncio
import time
from typing import List


# Import wait_n from the previous file
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Args:
        n (int): Number of concurrent coroutines to run
        max_delay (int): Maximum delay for each coroutine

    Returns:
        float: Average time per coroutine (total_time / n)
    """
    # Record start time
    start_time = time.time()

    # Run the async function
    asyncio.run(wait_n(n, max_delay))

    # Record end time
    end_time = time.time()

    # Calculate total execution time
    total_time = end_time - start_time

    # Return average time per coroutine
    return total_time / n
