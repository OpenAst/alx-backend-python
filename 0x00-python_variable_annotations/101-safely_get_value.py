#!/usr/bin/env python3
"""
This module make use of TypeVvar
"""

from typing import Dict, Optional, TypeVar

# Define a TypeVar for the value in the dictionary
V = TypeVar('V')

def safely_get_value(dct: Dict[str, V], key: str, default: Optional[V] = None) -> V:
    '''Safely get a value from a dictionary using the specified key.

    Args:
        dct (Dict[str, V]): A dictionary where keys are strings and values can be of any type.
        key (str): The key to look up in the dictionary.
        default (Optional[V], optional): The default value to return if the key is not present in the dictionary. Defaults to None.

    Returns:
        V: The value corresponding to the key in the dictionary, or the default value if the key is not present.
    '''
    if key in dct:
        return dct[key]
    else:
        return default
