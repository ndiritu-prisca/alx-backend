#!/usr/bin/python3
""" LIFOCache module
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    Inherits from BaseCaching
    """

    def __init__(self):
        """Initializes parent class"""
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """
        Assigns to the dictionary self.cache_data the item value for the key
        key.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.stack.remove(key)
            elif len(self.cache_data) >= self.MAX_ITEMS:
                removed_key = self.stack.pop()
                self.cache_data.pop(removed_key)
                print(f"DISCARD: {removed_key}")
            self.cache_data[key] = item
            self.stack.append(key)

    def get(self, key):
        """
        Returns the value in self.cache_data linked to key otherwise, None
        """
        if key is not None:
            return self.cache_data.get(key)
        return None
