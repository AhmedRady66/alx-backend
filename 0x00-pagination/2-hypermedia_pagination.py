#!/usr/bin/env python3
"""File for Dict representation of data"""
import csv
import math
from typing import List, Tuple, Dict, Any


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

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        """Return start and end index"""
        start_index = (page - 1) * page_size
        end_index = page * page_size

        return start_index, end_index

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return satrt and end page"""
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0
        start_idx, end_idx = self.index_range(page, page_size)
        return self.dataset()[start_idx:end_idx]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """Return dictionary containing the key-value for data"""
        data = self.get_page(page, page_size)
        total_data = len(self.dataset())
        total_pages = math.ceil(total_data / page_size)

        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages,
        }
