#!/usr/bin/env python3
""" FIFOCache module for implementing a FIFO caching system
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache implements a First-In-First-Out (FIFO) caching mechanism.
    """

    def __init__(self):
        """
        Initialize the cache and the order list to maintain the insertion
        order of keys.
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Add a key-value pair to the cache.
        If the cache exceeds the MAX_ITEMS limit,
        the oldest entry (first added) is discarded.
        Args:
            key: The key under which the item should be stored.
            item: The value to store in the cache.
        """
        if key is not None and item is not None:
            if len(self.cache_data) >=
            BaseCaching.MAX_ITEMS andkey not in self.cache_data:
                oldest_key = self.order.pop(0)
                print(f"DISCARD: {oldest_key}")
                del self.cache_data[oldest_key]

            self.order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve the value associated with the given key.
        Args:
            key: The key to look up in the cache.
        Returns:
            The value associated with the key, or None if
            the key doesn't exist.
        """
        return self.cache_data.get(key)
