#!/usr/bin/env python3
"""
This Module for task 6
"""
from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    compute the sum of ints and floats
    """

    return (float(sum(mxd_lst))
