"""
    Queue from 2 Stacks
    push(10)        s1 = [10],              s2 = [10]
    push(20)        s1 = [10, 20]           s2 = [20, 10]           get all elements from s1 and append to s2
    push(30)        s1 = [10, 20, 30]       s2 = [30, 20, 10]       get all elements from s1 and append to s2

    pop() = 10      s2.pop()    s1 = [20, 30]  s2 = [30, 20]    get all elements from s2 and append to s1
    
"""

class MyQueue(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, val):
        self.stack1.append(val)
        self.stack2 = []
        stack1_len = len(self.stack1)-1
        while stack1_len >= 0:
            self.stack2.append(self.stack1[stack1_len])
            stack1_len -= 1

    def pop(self):
        return_elem = self.stack2.pop()
        self.stack1 = []
        stack2_len = len(self.stack2)-1
        while stack2_len >= 0:
            self.stack1.append(self.stack2[stack2_len])
            stack2_len -= 1
        return return_elem
        # while len(self.stack1) > 1:
        #     self.stack2.append(self.stack1.pop())
        # last_item = self.stack1.pop()
        # while self.stack2:
        #     self.stack1.append(self.stack2.pop())
        # return last_item
if __name__=="__main__":

    q = MyQueue()
    q.push(10)
    q.push(20)
    q.push(30)
    print q.pop() # 10
    print q.pop() # 20
    q.push(40)
    q.push(50)
    print q.pop() # 30
    print q.pop() # 40
