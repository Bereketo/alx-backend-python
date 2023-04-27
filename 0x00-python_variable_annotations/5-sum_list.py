#!/usr/bin/env python3
"""A type-annotated function sum_list which takes
   a list input_list of floats as argument and returns their sum as a float.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """Argument:
            input_list: list of floats
       Returns:
            sum: summation of floats in the list
    """
    tot: float = 0.0
    for i in input_list:
        tot = tot + i
    return tot
