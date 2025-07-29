#!/usr/bin/env python3
"""
Function that concat strings
"""


def concat(str1: str, str2: str) -> str:
    """
    Args:
        str1 (string): string 1
        str2 (string): string 2

    Returns:
        str: combines str1 and str2

    Examples:
        >>> concat(egg, shell)
        eggshell
        >>> concat(bat, man)
        batman
        >>> concat(pizza, base)
        pizzabase
    """
    return str1 + str2
