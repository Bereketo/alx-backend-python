#!/usr/bin/env python3
"""Measure total time """
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure the total runtime and return it """
    data = [async_comprehension() for x in range(3)]
    start = time.time()
    await asyncio.gather(*data)
    end = time.time()
    return (end - start)
