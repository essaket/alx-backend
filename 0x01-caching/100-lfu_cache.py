#!/usr/bin/env python3
"""5. LFU Caching"""
BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    """A class LFU that inherits from BaseCaching and is a caching system"""
    def __init__(self):
        """Constructor"""
        super().__init__()
        self.keys = {}

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return
        if key is not None and item is not None\
                and self.cache_data.get(key) != item:
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                lfu_key = min(self.keys, key=self.keys.get)
                self.cache_data.pop(lfu_key)
                self.keys.pop(lfu_key)
                print("DISCARD:", lfu_key)
            self.keys[key] = self.keys.get(key, 0) + 1

    def get(self, key):
        """Return the value in self.cache_data linked to key"""
        if key is None or key not in self.cache_data:
            return None
        if key in self.keys:
            self.keys[key] += 1
        return self.cache_data.get(key)
