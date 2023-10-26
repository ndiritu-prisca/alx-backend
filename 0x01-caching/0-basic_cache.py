#!/usr/bin/python3
""" BasicCache module
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Inherits from BaseCaching
    """

    def put(self, key, item):
        """
        Assigns to the dictionary self.cache_data the item value for the key
        key.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Returns the value in self.cache_data linked to key otherwise, None
        """
        if key is not None:
            return self.cache_data.get(key)
        return None
