#!/usr/bin/env python3
"""2. LIFO Caching"""
BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """A class LIFO that inherits from BaseCaching and is a caching system"""
    def __init__(self):
        """Constructor"""
        super().__init__()
        self.last = None

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                last = self.last
                del self.cache_data[last]
                print("DISCARD: {}".format(last))
            self.last = key

    def get(self, key):
        """Return the value in self.cache_data linked to key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
