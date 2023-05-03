#!/usr/bin/evn python3

import asyncio
import random


async def wait_random(max_delay: int = 10) -> int:
    wait = random.uniform(0.0, float(max_delay))
    await asyncio.sleep(wait)
    return wait
