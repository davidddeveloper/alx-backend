#!/usr/bin/env python3
"""
    0-simple_helper_function.py: a function that takes two integer arguments
    page and page_size
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
        Args:
            page: the page
            page_size: and page_size
    """
    return (((page * page_size) - page_size), page_size)
