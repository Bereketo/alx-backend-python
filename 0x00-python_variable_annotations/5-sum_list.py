#!/usr/bin/env python3

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
