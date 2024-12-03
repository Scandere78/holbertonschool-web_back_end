#!/usr/bin/env python3
from typing import Union, Tuple


# function to_kv that takes a string and a number, and returns a tuple
def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    # Return a tuple with the string and (converted to float)
    return (k, float(v ** 2))
