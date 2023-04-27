#!/usr/bin/env python3
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Arguments:
            k: str
            v: int|float
       Returns:
            Tuple(k,v)
    """
    return (k, v**2)
