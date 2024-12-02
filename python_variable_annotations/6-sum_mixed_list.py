#!/usr/bin/env python3
from typing import List, Union

# Define the function sum_mixed_list that takes a list of integers and floats, and returns a float
def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    # Return the sum of the list, which will be of type float
    return float(sum(mxd_lst))
