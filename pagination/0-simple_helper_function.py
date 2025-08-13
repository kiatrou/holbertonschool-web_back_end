#!/usr/bin/env python3
"""
Pagination utility function for calculating index ranges.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate start and end indices for pagination.

    This function takes pagination parameters and returns the corresponding
    range of indices that should be used to slice a list for that page.

    Args:
        page (int): The page number (1-indexed). Must be >= 1.
        page_size (int): The number of items per page. Must be > 0.

    Returns:
        Tuple[int, int]: A tuple containing (start_index, end_index) where:
            - start_index: The starting index for the page (inclusive)
            - end_index: The ending index for the page
            (exclusive, for Python slicing)
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
