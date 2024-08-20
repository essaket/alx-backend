#!/usr/bin/env python3
"""3. LRU Caching"""
BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """A class LRU that inherits from BaseCaching and is a caching system"""
    def __init__(self):
        """Constructor"""
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key in self.keys:
                self.keys.remove(key)
            self.keys.append(key)
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                first = self.keys.pop(0)
                del self.cache_data[first]
                print("DISCARD: {}".format(first))

    def get(self, key):
        """Return the value in self.cache_data linked to key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
