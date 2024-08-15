#!/usr/bin/env python3
"""
Contains class with methods to create simple pagination from CSV data.
"""
import csv
from typing import List, Dict
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names."""
    
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Reads from the CSV file and returns the dataset.
        
        Returns:
            List[List]: The dataset without the header row.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip the header

        return self.__dataset

    @staticmethod
    def assert_positive_integer_type(value: int) -> None:
        """
        Asserts that the value is a positive integer.
        
        Args:
            value (int): The value to be checked.
        """
        assert isinstance(value, int) and value > 0, f"Value must be a positive integer, got {value}."

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieves a page of the dataset.
        
        Args:
            page (int): The page number (1-indexed).
            page_size (int): The number of records per page.
        
        Returns:
            List[List]: A list containing the requested page of the dataset.
        """
        self.assert_positive_integer_type(page)
        self.assert_positive_integer_type(page_size)

        dataset = self.dataset()
        start, end = index_range(page, page_size)

        if start >= len(dataset):
            return []  # Return an empty list if the page number exceeds the dataset size

        return dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Provides paginated data with metadata for hypermedia pagination.
        
        Args:
            page (int): The current page number (1-indexed).
            page_size (int): The number of records per page.
        
        Returns:
            Dict: A dictionary containing pagination metadata and the requested page's data.
        """
        self.assert_positive_integer_type(page)
        self.assert_positive_integer_type(page_size)

        dataset_length = len(self.dataset())
        total_pages = math.ceil(dataset_length / page_size)  # Calculate total pages

        data = self.get_page(page, page_size)
        info = {
            "page": page,
            "page_size": page_size if len(data) > 0 else 0,  # Ensure page_size is zero if no data
            "data": data,
            "total_pages": total_pages,
            "prev_page": page - 1 if page > 1 else None,
            "next_page": page + 1 if page < total_pages else None
        }

        return info
