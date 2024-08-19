#!/usr/bin/env python3
"""0. Basic dictionary"""
BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """A class inherits from BaseCaching and is a caching system"""
    def put(self, key, item):
        """Add an item in the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Return the value in self.cache_data linked to key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
