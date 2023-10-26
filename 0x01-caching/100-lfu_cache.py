#!/usr/bin/python3
""" LFUCache module
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    Inherits from BaseCaching
    """

    def __init__(self):
        """Initializes parent class"""
        super().__init__()
        self.uses = dict()

    def put(self, key, item):
        """
        Assigns to the dictionary self.cache_data the item value for the key
        key.
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if key not in self.cache_data:
                    removed_key = min(self.uses, key=self.uses.get)
                    del self.cache_data[removed_key]
                    del self.uses[removed_key]
                    print(f"DISCARD: {removed_key}")
            if key in self.cache_data:
                self.uses[key] += 1
            else:
                self.uses[key] = 1
            self.cache_data[key] = item

    def get(self, key):
        """
        Returns the value in self.cache_data linked to key otherwise, None
        """
        if key is not None:
            if key in self.cache_data:
                self.uses[key] += 1
                return self.cache_data.get(key)
        return None
