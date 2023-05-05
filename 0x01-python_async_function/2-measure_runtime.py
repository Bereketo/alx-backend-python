#!/usr/bin/env python3
"""Measure the run time of async function"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Arguments:
            n: int
            max_delay: int
       Returns:
            total-time: float
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    return (time.time() - start) / n
