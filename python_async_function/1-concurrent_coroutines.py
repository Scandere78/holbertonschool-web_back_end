import asyncio
import importlib
from typing import List

wait_random = importlib.import_module("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Coroutine qui exécute `wait_random` n fois en parallèle
    et retourne les délais triés par ordre croissant.

    Args:
        n (int): Nombre de coroutines à exécuter.
        max_delay (int): Durée maximale pour chaque attente.

    Returns:
        List[float]: Liste des délais triés par ordre croissant.
    """
    delays = []
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
