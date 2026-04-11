#!/usr/bin/env python3
"""
This module provides an asynchronous coroutine named wait_random.
The goal of this module is to demonstrate the basic syntax of
asynchronous programming in Python using the asyncio and random modules.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that takes in an integer argument (max_delay,
    with a default value of 10) named wait_random that waits for a random
    delay between 0 and max_delay (included and float value) seconds
    and eventually returns it as a floating point number.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

