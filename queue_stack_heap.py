#Queue

import Queue

q = Queue.Queue()
for i in range(5):
    q.put(i)

while not q.empty():
    print q.get()

#This will print 0, 1, 2, 3, 4

#from Queue import Queue
# q.put(element)
# q.empty()
# q.get()

#############################################
#############################################
#############################################

#Stack
stack = []

for i in range(3):
    stack.append(i)

while stack:
    print stack.pop()

#This will print 2,1,0
#In python, the list itself acts as a stack.
# s.append(element)
# s.pop() pop() method removes the last added element simulating the stack behavior
