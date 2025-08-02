#!/usr/bin/env python3
"""
Module containing measure_runtime function that measures the execution time
of running multiple async_comprehension calls in parallel.
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Execute async_comprehension four times in parallel
    and measure total runtime.

    This coroutine demonstrates the power of concurrent execution by running
    four instances of async_comprehension
    simultaneously using asyncio.gather().
    Even though each async_comprehension takes
    approximately 10 seconds to complete,
    running them in parallel results in a total
    execution time of roughly 10 seconds
    (not 40 seconds) because they execute concurrently.

    Returns:
        float: Total execution time in seconds (approximately 10 seconds)

    Example:
        >>> runtime = await measure_runtime()
        >>> print(f"Total runtime: {runtime:.2f} seconds")
        Total runtime: 10.02 seconds

    Note:
        This demonstrates that concurrent execution
        allows multiple async operations
        to run "at the same time" rather than sequentially.
        The total time is
        determined by the longest-running operation,
        not the sum of all operations.
    """
    start_time = time.time()
    results = await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_time = time.time()
    return end_time - start_time
