"""
Leetcode 141: https://leetcode.com/problems/linked-list-cycle/

    Find if linked-list has cycle
        1. use visited flag or store visited nodes in a set (extra storage space)
        2. use fast_ptr, slow_ptr approach.

    Find the length of cycle if linked-list has cycle.
        1. use fast_ptr, slow_ptr approach
            10 -> 20 -> 30 -> 40 -> 50
                        |            |
                        90 <- 80 <- 70
                        |      |
                        n     slow
                              fast

        slow and fast pointer meet at node 80.
        n = slow.next = 90
        while n != slow:
            len_of_loop += 1
            n = n.next
"""
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def get_linkedlist():
    n = ListNode(10)
    n1 = ListNode(20)
    n2 = ListNode(30)
    n3 = ListNode(40)
    n4 = ListNode(50)
    n5 = ListNode(60)
    n5.next = n2
    n.next = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    return n

def get_ll_size1():
    n = ListNode(10)
    n.next = n
    return n

def has_cycle(root):
    if not root:
        return
    slow_ptr = root
    fast_ptr = root
    while fast_ptr != None and fast_ptr.next != None:
        fast_ptr = fast_ptr.next.next
        slow_ptr = slow_ptr.next
        if fast_ptr == slow_ptr:
            return True

    return False

def cycle_length(root):
    if root is None:
        return 0
    cycle_len = 1
    cycle_detected = False
    fast_ptr = root
    slow_ptr = root
    while fast_ptr != None and fast_ptr.next != None:
        fast_ptr = fast_ptr.next.next
        slow_ptr = slow_ptr.next
        if slow_ptr == fast_ptr:
            cycle_detected = True
            break
    if cycle_detected is True:
        n = slow_ptr.next
        while n != slow_ptr:
            cycle_len += 1
            n = n.next
    else:
        cycle_len = 0
    return cycle_len



if __name__=="__main__":

    n = get_linkedlist()
    #n = get_ll_size1()
    print has_cycle(n)
    print cycle_length(n)