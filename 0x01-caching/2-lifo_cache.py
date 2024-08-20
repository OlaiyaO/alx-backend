#!/usr/bin/env python3
""" LIFOCache module for implementing a LIFO caching system
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache implements a Last-In-First-Out (LIFO) caching mechanism.
    """

    def __init__(self):
        """
        Initialize the cache and an order list to track the order of keys.
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Add a key-value pair to the cache.
        If the cache exceeds the MAX_ITEMS limit, the most recently added entry (last added) is discarded.
        Args:
            key: The key under which the item should be stored.
            item: The value to store in the cache.
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                last_key = self.order.pop()
                print(f"DISCARD: {last_key}")
                del self.cache_data[last_key]

            if key in self.order:
                self.order.remove(key)
            
            self.order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve the value associated with the given key.
        Args:
            key: The key to look up in the cache.
        Returns:
            The value associated with the key, or None if the key doesn't exist.
        """
        return self.cache_data.get(key)
