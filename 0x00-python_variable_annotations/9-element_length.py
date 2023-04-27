#!/usr/bin/env python3

from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Arguments:
            lst: iterable sequence
       Returns:
            List[Tuple[sequence, int]] -> list which contains tuple which
                                          in turn contans sequence and float.
    """
    return [(i, len(i)) for i in lst]
