#!/usr/bin/env python3
"""Module that measures the runtime of asynchronous coroutines."""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the average execution time of wait_n.

    Args:
        n (int): Number of coroutines.
        max_delay (int): Maximum delay.

    Returns:
        float: Average time (total time divided by n).
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()

    total_time = end - start
    return total_time / n
