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

# If you ever want to implement a Stack or a Queue,
#   use linked-list. Arrays are good for random access
#   but in Stack/Queue, random access A[i] is not required.

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

#############################################
#############################################
#############################################
###         Heap                    #########

#Calculate TOP-k frequent elements
#[1,1,1,1,2,2,3] k=2 then return [1,2]
import heapq
def top_k(data, k):
    top_k_elements = []
    heap = []
    map = {}
    for num in data:
        if map.get(num, None) is None:
            map[num] = 1
        else:
            map[num] += 1

    print map
    for key in map:
        heapq.heappush(heap, (-map.get(key), key))

    for _ in range(k):
        top_k_elements.append(heapq.heappop(heap)[1])

    return top_k_elements

#
#  ** Python only has min-heap implemented.
#
#    import heapq
#    data = []
# 1. heapq.heappush(data, elem)
# 2. elem = heapq.heappop(data)
# 3. heapq.heapify([10,2,7,3]) #sort the list as heap data structure
#
# 4. If you push tuple (10, a), (4, b), (12, c) into heap then it is stored
#   accordingly (4,b)->(10,a)->(12,c)
#
#
data = [(10,'a'), (4, 'b'), (12, 'c')]
heap = []
for val in data:
    heapq.heappush(heap, val)

while heap:
    print heapq.heappop(heap)
# (4, 'b'),(10, 'a'),(12,'c')


