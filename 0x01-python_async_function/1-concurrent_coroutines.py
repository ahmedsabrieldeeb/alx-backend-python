#!/usr/bin/env python3
"""The basics of async"""

import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> float:
    """
    Waits for a random delay between 0 and `max_delay` seconds and returns it

    Args:
        n (int): The number of times to call wait_random
        max_delay (int): The maximum random delay

    Returns:
        ret (float): The list of all the delays
    """
    delays = [wait_random(max_delay) for _ in range(n)]
    ret = await asyncio.gather(*delays)
    ret.sort()
    return ret
