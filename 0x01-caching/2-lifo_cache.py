#!/usr/bin/python3

"""
LIFOCache module
"""

from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    """ caching system
    """
    def __init__(self):
        super().__init__()
        self.keys_order = []

    def put(self, key, item):
        if key is None or item is None:
            return

        # If the cache is full, remove the last item (LIFO behavior)
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key = self.keys_order.pop()
            del self.cache_data[last_key]
            print("DISCARD:", last_key)

        self.cache_data[key] = item
        self.keys_order.append(key)

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
