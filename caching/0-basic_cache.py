#!/usr/bin/env python3
""" BasicCache module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache defines a simple caching system that inherits from BaseCaching.
    """

    def put(self, key, item):
        """
        Add an item inthe cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key
        """
        return self.cache_data.get(key, None)
