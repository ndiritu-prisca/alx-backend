#!/usr/bin/env python3
"""A simple helper function"""


def index_range(page: int, page_size: int) -> tuple:
    """
    A function that calculates the start and end indices for pagination.
    """
    if (page <= 0 or page_size <= 0):
        raise ValueError("Both page and page_size must be positive integers.")

    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size

    return start_idx, end_idx
