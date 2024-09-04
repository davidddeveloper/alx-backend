"""
    1-fifo_cache.py: Implements the fifo chaching queue policy

"""

BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """
        Represents: fifo caching algo

    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
            Assign self.cache_date the item value for the key
            Args:
                key: the key to be inserted
                item: the value to be inserted
        """
        self.cache_data[key] = item

        if key is not None or item is not None:
            if len(self.cache_data) > FIFOCache.MAX_ITEMS:
                # discard the first item
                key_discarded = list(self.cache_data.keys())[0]
                del self.cache_data[key_discarded]
                print("DISCARD:", key_discarded)

    def get(self, key):
        """
            Get the value for key in self.cache_data
            Args:
                key: the key to get
        """

        return self.cache_data.get(key)
