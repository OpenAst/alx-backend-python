#!/usr/bin/env python3
"""
This module adds two float
"""

def add(a: float, b: float) -> float:
    '''Add two floats and return their sum.

    Args:
        a (float): The first float.
        b (float): The second float.

    Returns:
        float: The sum of the input floats.
    '''
    return float(sum(a, b))
