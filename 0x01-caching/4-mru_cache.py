#!/usr/bin/env python3
""" MRUCache module for implementing an MRU caching system
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache implements a Most Recently Used (MRU) caching mechanism.
    """

    def __init__(self):
        """
        Initialize the cache and a usage list to track the order of key access.
        """
        super().__init__()
        self.usage = []

    def put(self, key, item):
        """
        Add a key-value pair to the cache.
        If the cache exceeds the MAX_ITEMS limit, the most recently used entry is discarded.
        Args:
            key: The key under which the item should be stored.
            item: The value to store in the cache.
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                most_recent_key = self.usage.pop(-1)
                print(f"DISCARD: {most_recent_key}")
                del self.cache_data[most_recent_key]
            
            if key in self.usage:
                self.usage.remove(key)
            
            self.usage.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve the value associated with the given key.
        Updates the usage order since the key has been accessed.
        Args:
            key: The key to look up in the cache.
        Returns:
            The value associated with the key, or None if the key doesn't exist.
        """
        if key is not None and key in self.cache_data:
            self.usage.remove(key)
            self.usage.append(key)
            return self.cache_data[key]
        return None
