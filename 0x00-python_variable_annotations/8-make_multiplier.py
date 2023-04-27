#!/usr/bin/env python3

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Arguments:
            multiplier: float
       Returns:
            callable - a function
    """
    def multiply(x: float) -> float:
        """Returns x multiplied by multiplier """
        return x * multiplier
    return multiply
