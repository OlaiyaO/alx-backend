#!/usr/bin/env python3
""" BasicCache module for caching key-value pairs
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Basic caching system using key-value pairs
    """

    def __init__(self):
        """
        Initialize the cache using the parent class __init__ method
        """
        super().__init__()

    def put(self, key, item):
        """
        Add a key-value pair to the cache
        Args:
            key: The key under which the item should be stored
            item: The value to store in the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve the value associated with the key
        Args:
            key: The key to look up in the cache
        Returns:
            The value associated with the key, or None if the key doesn't exist
        """
        return self.cache_data.get(key)
