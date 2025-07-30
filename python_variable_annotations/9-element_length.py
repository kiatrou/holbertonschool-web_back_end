#!/usr/bin/env python3
"""
Function that takes a list and
returns a tuple of the list
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Args:
        lst (Iterable[Sequence]): An iterable (list, tuple, etc.) containing
            sequences. Each element must be something that has a length
            (str, list, tuple, etc.).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each tuple contains:
            - First element: The original sequence from the input
            - Second element: The length of that sequence as an integer

    Examples:
        >>> element_length(["hello", "world", "python"])
        [('hello', 5), ('world', 5), ('python', 6)]

        >>> element_length([["a", "b"], ["x", "y", "z"]])
        [(['a', 'b'], 2), (['x', 'y', 'z'], 3)]

        >>> element_length(("abc", [1, 2, 3, 4], "hi"))
        [('abc', 3), ([1, 2, 3, 4], 4), ('hi', 2)]
    """
    return [(i, len(i)) for i in lst]
