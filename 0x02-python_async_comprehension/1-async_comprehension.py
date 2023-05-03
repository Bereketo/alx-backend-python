#!/usr/bin/env python3
"""coroutine will collect 10 random numbers using an async comprehensing """
import asyncio
from typing import List, Any
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[Any]:
    """The coroutine will collect 10 random numbers
       using an async comprehensing
    """
    res = [x async for x in async_generator()]
    return res
