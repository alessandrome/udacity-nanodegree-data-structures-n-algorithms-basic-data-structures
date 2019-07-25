from collections import OrderedDict


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self._dict = OrderedDict()
        if self.capacity < 1:
            print('Warning: cache with zero capacity can\'t store any data!')
        pass

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if self.capacity < 1:
            return -1
        if key in self._dict:
            popped = self._dict.pop(key)
            self._dict[key] = popped
            return popped
        return -1

    def set(self, key, value):
        if self.capacity < 1:
            return
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if key in self._dict:
            self._dict.pop(key)
            self._dict[key] = value
        else:
            if len(self._dict) >= self.capacity:
                self._dict.popitem(last=False)
            self._dict[key] = value


# Simple test
print('# SIMPLE TEST #')
our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)
print(our_cache.get(1))  # returns 1
print(our_cache.get(2))  # returns 2
print(our_cache.get(9))  # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))  # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

# Editing Test
print('\n# EDITING TEST #')
our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)
our_cache.set(5, 5)
our_cache.set(1, 10)  # Update key one. Now key one is not the last recently used key
our_cache.set(6, 6)
print(our_cache.get(2))  # returns -1 because the cache reached it's capacity and 2 was the least recently used entry
print(our_cache.get(1))  # returns 10 because this is still in the LRU cache and updated


# Edge Test
print('\n# EDITING TEST #')
our_cache = LRU_Cache(0)

# Every operation should be useless
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
print(our_cache.get(1))  # returns 1 because this is still in the LRU cache
print(our_cache.get(2))  # returns -1 because the cache reached it's capacity and 2 was the least recently used entry
print(our_cache.get(3))  # returns 1 because this is still in the LRU cache
