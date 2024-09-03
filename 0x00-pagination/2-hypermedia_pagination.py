#!/usr/bin/env python3
"""
    1-simple_pagination.py:
    implements get_page to return a paginated data from csv
    implements get_hyper
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

    def get_hyper(self, page: int = 1, page_size: int = 10):
        """
            Args:
                page: current page number
                page_size: length of the returned dataset

        """

        data = self.get_page(page, page_size)
        total_items = len(self.__dataset)
        condition = (1 if total_items % page_size > 0 else 0)
        total_pages = (total_items // page_size) + condition

        data_dictionary = {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": None if (page + 1 > total_pages) else page + 1,
            "prev_page": None if page - 1 == 0 else page - 1,
            "total_pages": total_pages
        }

        return data_dictionary
