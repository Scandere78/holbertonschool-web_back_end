#!/usr/bin/env python3
'''Async Comprehensions'''
from typing import List
Vector = List[float]

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Vector:
    ''' Collect 10 random numbers using async_generator '''
    return [y async for y in async_generator()]
