#!/usr/bin/env python3
"""
Módulo para demostrar comprensiones de listas asíncronas.
"""


from typing import List
import asyncio

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Recolecta 10 números aleatorios usando una comprensión asíncrona
    sobre el generador async_generator.
    """
    return [i async for i in async_generator()]
