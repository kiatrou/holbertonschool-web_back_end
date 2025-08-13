#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination

This module provides a Server class that implements
pagination which is resilient
to data deletions. Instead of using page numbers,
it uses index-based pagination
to ensure users don't miss items when data is removed between queries.
"""

import csv
import math
from typing import List, Dict


class Server:
    """
    Server class to paginate a database of popular baby
    names with deletion resilience.

    This class provides index-based pagination
    that remains consistent even when
    rows are deleted from the dataset. It uses indexed access instead of page
    numbers to ensure users can continue pagination without missing items.

    Attributes:
        DATA_FILE (str): The filename of the CSV data file.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        Initialize the Server instance.

        Sets up private caches for both the raw dataset and the indexed dataset
        that will be populated when first accessed.
        """
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """
        Get the cached dataset without headers.

        Loads the CSV file on first call and caches the result. The header row
        is automatically removed from the dataset.

        Returns:
            List[List]: The dataset as a list of rows, where each row is a list
                       of values. Header row is excluded.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Get dataset indexed by sorting position, starting at 0.

        Creates a dictionary where keys are the original indices and values
        are the corresponding rows. This allows for stable indexing even
        when some rows might be deleted.

        Returns:
            Dict[int, List]: Dictionary mapping original indices to rows.
            Keys are integers starting from 0, values are
            lists representing individual rows.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Get deletion-resilient paginated data using index-based pagination.

        This method provides pagination that remains consistent even when rows
        are deleted from the dataset. Instead of using page numbers, it uses
        direct indexing to ensure users don't miss items when data changes
        between requests.

        Args:
            index (int, optional): The starting index for the page. If None,
            defaults to 0. Must be a valid index in the dataset.
            page_size (int, optional): The number of rows per page.
            Must be a positive integer. Defaults to 10.

        Returns:
            Dict: A dictionary containing pagination
            data and metadata with keys:
                - index (int): Current start index of the returned page
                - next_index (int): Next index to query
                with (first item after current page)
                - page_size (int): Current page size (number of items returned)
                - data (List[List]): The actual page data (list of rows)

        Raises:
            AssertionError: If index is not in a valid range for the dataset.

        Examples:
            >>> # Get first page starting from index 0
            >>> server.get_hyper_index(0, 5)
            {
                'index': 0,
                'next_index': 5,
                'page_size': 5,
                'data': [['Emma', 'F', '2020', '15581'], ...]
            }

            >>> # Continue from next_index, even if some rows were deleted
            >>> server.get_hyper_index(10, 5)  # Rows 3, 6, 7 deleted
            {
                'index': 10,
                'next_index': 15,
                'page_size': 5,
                'data': [['row at original index 10'], ...]
                # Still gets correct rows
            }

            >>> # Default index behavior
            >>> server.get_hyper_index()  # Same as get_hyper_index(0, 10)
            {
                'index': 0,
                'next_index': 10,
                'page_size': 10,
                'data': [...]
            }

        Note:
            The method ensures that users receive exactly page_size items (when
            available) starting from the specified index, regardless of any
            deletions that may have occurred in the dataset. The next_index
            value can be used for the subsequent request
            to continue pagination.
        """
        # Set default index if None provided
        if index is None:
            index = 0

        # Get the indexed dataset
        indexed_data = self.indexed_dataset()

        # Validate that index is in valid range
        assert 0 <= index < len(indexed_data), f"Index {index} is out of range"

        # Collect page_size items starting from the given index
        data = []
        current_index = index
        collected = 0

        # Continue collecting until we have page_size items or run out of data
        while collected < page_size and current_index < len(indexed_data):
            # Only add the item if it still exists in the indexed dataset
            if current_index in indexed_data:
                data.append(indexed_data[current_index])
                collected += 1
            current_index += 1

        # Calculate next index (first index after the current page)
        next_index = current_index

        return {
            "index": index,
            "next_index": next_index,
            "page_size": len(data),
            "data": data
        }
