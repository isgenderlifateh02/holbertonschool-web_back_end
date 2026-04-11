#!/usr/bin/env python3
"""
This module provides an asynchronous coroutine called wait_random that
illustrates the basics of the async and await syntax in Python. It
leverages the random module to generate non-deterministic sleep durations.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronously waits for a random amount of time and returns the
    duration of the delay.

    Args:
        max_delay (int): The maximum number of seconds to wait.

    Returns:
        float: The actual number of seconds spent waiting.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


