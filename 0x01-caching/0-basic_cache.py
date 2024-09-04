"""
    0-basic_cache.py: Basic dictionary for implementing caching

"""
BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """Represents a basic cache"""
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
            Assign self.cache_date the item value for the key
            Args:
                key: the key to be inserted
                item: the value to be inserted

        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
            Get the value for key in self.cache_data
            Args:
                key: the key to get

        """
        return self.cache_data.get(key)
