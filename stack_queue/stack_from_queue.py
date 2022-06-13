from Queue import Queue
"""
                q1 = []             ,q2 = []
    push(10) => q1 = [10]           ,q2 = []
    push(20) => q1 = [10, 20]       ,q2 = []
    push(30) => q1 = [10, 20, 30]   ,q2 = []
    
    pop()   =>
               q1 = []      , q2 = [10,20]
               q1 = [10, 20], q2 = []
            return 30
    
    pop()   =>
               q1 = []      , q2 = [10]
               q1 = [10]    , q2 = []
            return 20
            
"""
class MyStack(object):
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def push(self, val):
        self.queue1.put(val)

    def pop(self):
        while self.queue1.qsize() > 1:
            self.queue2.put(self.queue1.get())
        last_item = self.queue1.get()
        while not self.queue2.empty():
            self.queue1.put(self.queue2.get())
        return last_item

if __name__=="__main__":
    stack = MyStack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print stack.pop()     # -> 30
    print stack.pop()     # -> 20