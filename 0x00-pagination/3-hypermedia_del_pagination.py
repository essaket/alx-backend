#!/usr/bin/env python3
"""3. Deletion-resilient hypermedia pagination"""
import csv
import math
from typing import List, Dict, Tuple


class Server:
    """Server class to paginate a database of popular baby names"""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Return the pagination parameters"""
        data_size = len(self.dataset())

        # Validate the index range
        assert index is None or (0 <= index < data_size)

        # Calculate the next index for pagination
        if index is None:
            next_index = 0
        else:
            next_index = min(index + page_size, data_size)

        # Retrieve data for the current page
        data = self.dataset()[index:next_index]

        # Construct pagination parameters
        pagination_params = {
            "index": index,
            "next_index": next_index if next_index < data_size else None,
            "page_size": len(data),
            "data": data
        }

        return pagination_params
