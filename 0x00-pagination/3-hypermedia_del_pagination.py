#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
            Args:
                index: the current start index of the return page.
                page_size: the current page size

        """

        total_items = len(self.__indexed_dataset)
        assert index < total_items

        while self.__indexed_dataset.get(index) is None:
            index += 1

        data = self.__indexed_dataset.get(index)
        condition = (1 if total_items % page_size > 0 else 0)
        total_pages = (total_items // page_size) + condition

        # get correct next_index
        next_index = index + page_size
        if (index + page_size) > total_pages:
            next_index = None

        data = {
            "index": index,
            "data": data,
            "page_size": page_size,
            "next_index": next_index
        }

        return data
