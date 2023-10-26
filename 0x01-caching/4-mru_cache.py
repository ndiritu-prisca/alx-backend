#!/usr/bin/python3
""" MRUCache module
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
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
            if key in self.cache_data:
                self.stack.remove(key)
                self.stack.append(key)
                return self.cache_data[key]
        return None
