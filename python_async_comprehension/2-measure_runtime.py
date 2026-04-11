#!/usr/bin/env python3
"""
Módulo para medir el tiempo de ejecución en paralelo.
"""


import asyncio
import time

# Importación dinámica del archivo anterior
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Ejecuta async_comprehension cuatro veces en paralelo usando
    asyncio.gather y devuelve el tiempo total de ejecución.
    """
    start_time = time.perf_counter()

    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    end_time = time.perf_counter()
    return end_time - start_time
