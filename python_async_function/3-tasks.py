#!/usr/bin/env python3
"""
A function that takes an integerand returns a
asyncio.Task
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    """
    Create an asyncio Task that will execute
    wait_random with the given max_delay.

    Args:
        max_delay (int): Maximum delay in seconds for the wait_random function.
                        Defaults to 10.

    Returns:
        asyncio.Task: A Task object that can be
        awaited to run wait_random(max_delay).
    """
    return asyncio.create_task(wait_random(max_delay))
