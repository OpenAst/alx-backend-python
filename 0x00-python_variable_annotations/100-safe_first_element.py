#!/usr/bin/env python3
"""
duck-typing module
"""

from typing import Any, Optional, List

def safe_first_element(lst: List[Any]) -> Optional[Any]:
    '''Get the first element of a list safely.

    Args:
        lst (list): A list of elements.

    Returns:
        Any: The first element of the list, or None if the list is empty.
    '''
    if lst:
        return lst[0]
    else:
        return None
