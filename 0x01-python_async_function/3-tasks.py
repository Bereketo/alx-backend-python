#!/usr/bin/env python3
"""Creates a task """
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Arguments:
            max_delay: int
       Returns:
            asyncio.Task
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
