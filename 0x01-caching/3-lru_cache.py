#!/usr/bin/python3

"""
LRUCache module
"""

from base_caching import BaseCaching

class LRUCache(BaseCaching):
    """
    caching system
    """
    def __init__(self):
        # initialization
        super().__init__()
        """When an item is accessed, it is moved to the end of the list
         signifying that it is the most recently used item
          item at the front of this list is the least recently used item
        """
        self.access_order = []

    def put(self, key, item):
        # asign the value to key
        if key is None or item is None:
            return

        # If the cache is full, remove the least recently used item
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru_key = self.access_order.pop(0) # pop first item of list
            del self.cache_data[lru_key]
            print("DISCARD:", lru_key)

        self.cache_data[key] = item
        self.access_order.append(key)
        self.move_to_front(key)

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None

        self.move_to_front(key)
        return self.cache_data[key]

    def move_to_front(self, key):
        """ Move the given key to the front of the access order list
        """
        if key in self.access_order:
            self.access_order.remove(key)
        self.access_order.append(key)
