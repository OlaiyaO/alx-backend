#!/usr/bin/env python3
""" LFUCache module for implementing an LFU caching system
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache implements a Least Frequently Used (LFU) caching mechanism.
    """

    def __init__(self):
        """
        Initialize the cache with a usage list and a frequency dictionary to track the usage frequency of keys.
        """
        super().__init__()
        self.usage = []  # Tracks the order of key usage
        self.frequency = {}  # Tracks the frequency of access for each key

    def put(self, key, item):
        """
        Add a key-value pair to the cache.
        If the cache exceeds the MAX_ITEMS limit, the least frequently used entry is discarded.
        If multiple keys have the same lowest frequency, the least recently used among them is discarded.
        Args:
            key: The key under which the item should be stored.
            item: The value to store in the cache.
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                # Find the least frequently used (LFU) key(s)
                lfu = min(self.frequency.values())
                lfu_keys = [k for k, v in self.frequency.items() if v == lfu]
                
                if len(lfu_keys) > 1:
                    # If there's a tie, discard the least recently used (LRU) among the LFU keys
                    lru_lfu = {k: self.usage.index(k) for k in lfu_keys}
                    discard = self.usage[min(lru_lfu.values())]
                else:
                    discard = lfu_keys[0]

                print(f"DISCARD: {discard}")
                del self.cache_data[discard]
                self.usage.remove(discard)
                del self.frequency[discard]

            # Update or add the key and its usage frequency
            self.frequency[key] = self.frequency.get(key, 0) + 1
            
            if key in self.usage:
                self.usage.remove(key)
            
            self.usage.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve the value associated with the given key.
        Updates the usage frequency and order since the key has been accessed.
        Args:
            key: The key to look up in the cache.
        Returns:
            The value associated with the key, or None if the key doesn't exist.
        """
        if key is not None and key in self.cache_data:
            self.usage.remove(key)
            self.usage.append(key)
            self.frequency[key] += 1
            return self.cache_data[key]
        return None
