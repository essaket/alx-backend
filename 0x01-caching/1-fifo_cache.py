#!/usr/bin/env python3
"""1. FIFO caching"""
BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """A class FIFO that inherits from BaseCaching and is a caching system"""
    def __init__(self):
        """Constructor"""
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                first_key = next(iter(self.cache_data))
                del self.cache_data[first_key]
                print("DISCARD: {}".format(first_key))
            self.cache_data[key] = item

    def get(self, key):
        """Return the value in self.cache_data linked to key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
