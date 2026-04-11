#!/usr/bin/env python3
"""Module that demonstrates basic asynchronous coroutine usage."""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronously waits for a random delay between 0 and max_delay seconds.

    Args:
        max_delay (int): The maximum delay in seconds.

    Returns:
        float: The actual delay waited.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
