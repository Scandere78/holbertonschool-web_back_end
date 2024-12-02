#!/usr/bin/env python3
from typing import Union, Tuple

# Define the function to_kv that takes a string and a number (int or float), and returns a tuple
def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    # Return a tuple with the string and the square of the number (converted to float)
    return (k, float(v ** 2))
