#!/usr/bin/python3
""" FIFOCache module
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Inherits from BaseCaching
    """

    def __init__(self):
        """Initializes parent class"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """
        Assigns to the dictionary self.cache_data the item value for the key
        key.
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                removed_key = self.queue.pop(0)
                self.cache_data.pop(removed_key)
                print(f"DISCARD: {removed_key}")
            self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """
        Returns the value in self.cache_data linked to key otherwise, None
        """
        if key is not None:
            return self.cache_data.get(key)
        return None
