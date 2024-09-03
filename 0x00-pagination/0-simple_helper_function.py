#!/usr/bin/env python3
"""
    0-simple_helper_function.py: a function that takes two integer arguments page and page_size
"""

def index_range(page, page_size):
    """
        page: the page 
        page_size: and page_size
    """
    return ((page * page_size) - page_size, page_size)
