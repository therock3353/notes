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


    class LRUCache(object):
        def __init__(self, capacity):
            self.capacity = capacity
            self.data = []

        def get(self, key):
            if key in self.data:
                value = self.data.pop(key)
                self.data[key] = value
                key exists in dictionary hence need to remove it and add it back so
                the key access is recorded in most frequently accessed key

        def put(self, key, value):
            if key exists in self.data:
                remove key
                add key, value back to self.data
            else:
                key doesn't exist so we need to add new element in self.data
                so check if the size of self.data is beyond capacity
                if len(self.data) >= self.capacity:
                    remove the first item added to self.data
                    self.data.popitem(last=False)
                    self.data[key] = value
                else:
                    self.data.pop(key, None)
                    self.data[key] = value


"""
from collections import OrderedDict

class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = OrderedDict()

    def get(self, key):
        if key in self.data:
            val = self.data.pop(key, None)
            self.data[key] = val
            return val
        return -1

    def put(self, key, value):
        if key in self.data:
            self.data.pop(key, None)
            self.data[key] = value
        else:
            if len(self.data) >= self.capacity:
                self.data.popitem(last=False)
                self.data[key] = value
            else:
                self.data.pop(key, None)
                self.data[key] = value
    
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