from Queue import Queue
from heapq import heappush, heappop

class MyQueue(object):
    def __init__(self):
        self.q = Queue()
        self.max = None
        self.heap = []

    def push(self, value):
        self.q.put(value)
        heappush(self.heap, value*-1)
        self.max = self.heap[0] * -1

    def pop(self):
        if self.q.qsize() > 0:
            value = self.q.get()
            if value == self.max:
                heappop(self.heap)
                self.max = self.heap[0] * -1
            else:
                self.heap.remove(value * -1)

    def getMax(self):
        return self.max if self.q.qsize() > 0 else None

    def print_elem(self):
        return [i for i in self.q.queue]

if __name__=="__main__":

    queue = MyQueue()
    data = [2, 25, 20, 4 ,5, 10, 6]
    for i in data:
        queue.push(i)
        #print "max: {}, queue {}".format(queue.getMax(), queue.print_elem())
        #print queue.heap

    for _ in data:
        queue.pop()
        print "max: {}, queue {}".format(queue.getMax(), queue.print_elem())
        print queue.heap
