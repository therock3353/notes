"""
    We can use python 2.7's ordered dict data structure.
    This data structure is more like a linked-hashmap where keys
    are stored in a doubly linked-list. The benefit of this is
    that keys insertion order is maintained.
    The data-structure supports, popitem(last=False) that removes the first
    stored item from map. ie supports FIFO deletion order.
    additional simplified example:
        https://www.geeksforgeeks.org/ordereddict-in-python/

    Note:
        self.store.popitem(last=False) api call.

"""
from collections import OrderedDict

class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.store = OrderedDict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.store:
            value = self.store.pop(key)
            self.store[key] = value
            return value
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if len(self.store) < self.capacity:
            if key not in self.store:
                self.store[key] = value
            else:
                self.store.pop(key)
                self.store[key] = value
        else:
            if key not in self.store:
                self.store.popitem(last=False)
                self.store[key] = value
            else:
                self.store.pop(key)
                self.store[key] = value

lru = LRUCache(2)
lru.put(1,1)
lru.put(2,2)
print(lru.get(1))
lru.put(3,3)
print(lru.get(2))
lru.put(4,4)
print(lru.get(1))
print(lru.get(3))
print(lru.get(4))

