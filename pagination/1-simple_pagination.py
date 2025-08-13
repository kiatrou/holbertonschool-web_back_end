#!/usr/bin/env python3

import csv
import math
from typing import List, Tuple


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get a specific page of data from the CSV dataset.

        This method reads the Popular_Baby_Names.csv file
        and returns the specified
        page of data based on pagination parameters.
        Uses the index_range function
        to calculate the correct slice of data to return.

        Args:
            page (int, optional): The page number to retrieve (1-indexed).
            Must be a positive integer. Defaults to 1.
            page_size (int, optional): The number of rows per page.
            Must be a positive integer. Defaults to 10.

        Returns:
            List[List]: A list of rows for the requested page,
            where each row is
                represented as a list of values. Returns an empty list if
                the requested page is out of range for the dataset.
            """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        with open('Popular_Baby_Names.csv', mode='r') as file:
            csvFile = csv.reader(file)
            rows = []
            for row in csvFile:
                rows.append(row)
        start, end = index_range(page, page_size)
        page_data = rows[start:end]
        return page_data
