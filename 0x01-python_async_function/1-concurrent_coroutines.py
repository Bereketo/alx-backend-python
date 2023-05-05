#!/usr/bin/env python3
"""Contains wait_n function which returns
   delay
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Arguments:
            n: int
            max_delay: int
       Returns:
            list of delays
    """
    delays = [wait_random(max_delay) for i in range(n)]
    all_delays = await asyncio.gather(*delays)
    return sorted(all_delays)
