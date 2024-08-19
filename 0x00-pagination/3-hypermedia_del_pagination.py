#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination.
"""

import csv
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Loads and caches the dataset.

        Returns:
            List[List]: The cached dataset without the header row.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip the header row.

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Creates an indexed version of the dataset that can handle deletions.

        Returns:
            Dict[int, List]: Dataset indexed by position, starting at 0.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Returns a delition-resilient dictionary.

        Args:
            index (int): The start index for pagination.
            page_size (int): The number of records to return.

        Returns:
            Dict: Contains current index, next index, page size, and data.

        Raises:
            AssertionError: If index is out of range.
        """
        dataset = self.indexed_dataset()
        data_length = len(dataset)
        assert 0 <= index < data_length, "Index out of range."

        response = {
            'index': index,
            'data': [],
            'page_size': page_size,
            'next_index': None
        }

        current_index = index
        count = 0

        while count < page_size and current_index < data_length:
            item = dataset.get(current_index)
            if item is not None:
                response['data'].append(item)
                count += 1
            current_index += 1

        response['page_size'] = len(response['data'])

        if current_index < data_length:
            response['next_index'] = current_index
        else:
            response['next_index'] = None  # No more items after this page.

        return response
