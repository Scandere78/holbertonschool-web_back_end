#!/usr/bin/env python3
from typing import Callable


# make_multiplier that returns a function to multiply a number by multiplier
def make_multiplier(multiplier: float) -> Callable[[float], float]:
    # return a function that multiplies its input by the multiplier
    return lambda x: x * multiplier
