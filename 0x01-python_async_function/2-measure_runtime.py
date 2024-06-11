#!/usr/bin/env python3
"""The basics of async"""

import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the runtime

    Args:
        n (int): The number of times to call wait_random
        max_delay (int): The maximum random delay

    Returns:
        avg (float): The runtime per call (avergae)
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    avg = (end - start) / n
    return avg
