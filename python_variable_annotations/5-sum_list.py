#!/usr/bin/env python3
from typing import List


# Define the function sum_list that takes a list of flats and returns a float
def sum_list(input_list: List[float]) -> float:
    if not input_list:
        return 0.0

    total = 0.0
    for i in input_list:
        if isinstance(i, float):
            total += i
        else:
            raise TypeError("All elements in the list must be floats.")

    return total
