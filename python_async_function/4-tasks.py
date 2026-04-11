#!/usr/bin/env python3
"""Module that defines task_wait_n coroutine"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Run multiple tasks concurrently and return sorted delays.

    Args:
        n (int): number of tasks
        max_delay (int): maximum delay

    Returns:
        List[float]: sorted delays
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    delays = [await task for task in tasks]

    return sorted(delays)
