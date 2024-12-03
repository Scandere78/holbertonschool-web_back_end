#!/usr/bin/env python3
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Coroutine asynchrone qui attend un délai aléatoire entre 0 et max_delay.

    Args:
        max_delay (int): Durée maximale (en secondes) du délai. Par défaut, 10.

    Returns:
        float: Durée réelle (en secondes) du délai aléatoire.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
