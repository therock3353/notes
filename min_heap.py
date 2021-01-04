"""
    [0, 1, 2, 3, 4, 5, 6]
    [4,10,15,20,12,18,30]

    Child: 2*i+1    4 -> 10,15
           2*i+2    10-> 20,12
                    15-> 18,30

    Parent: (i-1)/2     18 -> i=5 -> (i-1)/2 -> 2 -> data[2] = 15
                        12 -> i=4 -> (i-1)/2 -> 1 -> data[1] = 10
                        20 -> i=3 -> (i-1)/2 -> 1 -> data[1] = 10
                        10 -> i=1 -> (i-1)/2 -> 0 -> data[0] = 4
                        15 -> i=2 -> (i-1)/2 -> 0 -> data[0] = 4
"""

class MinHeap(object):
    def __init__(self):
        self.data = []
        self.last = 0

    def _parent(self, i):
        return (i-1)/2

    def _left_child(self, i):
        return 2*i+1

    def _right_child(self, i):
        return 2*i+2

    def insert(self, e):
        self.data.append(e)
        self._bubble_up(self.last)
        self.last += 1

    def extract_min(self):
        pass

    def _bubble_up(self, current_node_ptr):
        if current_node_ptr == 0:
            return
        #current_node = current_node_ptr
        parent_ptr = self._parent(current_node_ptr)
        if self.data[parent_ptr] > self.data[current_node_ptr]:
            self.data[parent_ptr], self.data[current_node_ptr] = self.data[current_node_ptr], self.data[parent_ptr]
            current_node_ptr = parent_ptr
            self._bubble_up(current_node_ptr)

    def _bubble_down(self):
        pass


if __name__=="__main__":

    heap = MinHeap()
    heap.insert(4)
    heap.insert(10)
    heap.insert(2)
    heap.insert(12)
    heap.insert(14)
    heap.insert(6)
    heap.insert(3)
    heap.insert(5)
    heap.insert(1)

    print heap.data