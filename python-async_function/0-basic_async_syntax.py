#!/usr/bin/env python3
"""
Coroutine that takes an int as an argument that waits
for a random delay betwneen 0 and max_delay seconds
and eventually returns it
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay and returns it.
    
    Args:
        max_delay (int): Maximum delay in seconds (default: 10)
    
    Returns:
        float: The actual delay time that was waited
    """
    # Generate a random float between 0 and max_delay (inclusive)
    delay = random.uniform(0, max_delay)
    
    # Wait for the random delay
    await asyncio.sleep(delay)
    
    # Return the delay that was actually waited
    return delay
