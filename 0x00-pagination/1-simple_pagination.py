#!/usr/bin/env python3
"""Simple pagination"""

import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """
    A function that calculates the start and end indices for pagination.
    """
    if (page <= 0 or page_size <= 0):
        raise ValueError("Both page and page_size must be positive integers.")

    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size

    return start_idx, end_idx


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
        """Method that gets page"""
        assert isinstance(page, int) and isinstance(page_size, int), \
            "Both page and page_size must be integers."
        assert page > 0 and page_size > 0, \
            "Both page and page_size must be greater than 0."

        dataset = self.dataset()
        dataset_length = len(dataset)

        start_idx, end_idx = index_range(page, page_size)

        if start_idx >= dataset_length or start_idx < 0:
            return []

        return dataset[start_idx:end_idx]
