#!/usr/bin/env python3
"""
    1-simple_pagination.py: implements get_page to paginate a csv data

"""
import csv
import math
from typing import List


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
            Args:
                page: the page
                page_size: and page_size
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        # range to get: in the form (1, 7) or (page, page_size)
        index_range = (((page * page_size) - page_size), (page_size * page))
        # load the data
        self.dataset()
        try:
            return self.__dataset[index_range[0]:index_range[1]]
        except IndexError:
            return []
