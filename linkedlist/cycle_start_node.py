"""
Leetcode 142: https://leetcode.com/problems/linked-list-cycle-ii/

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

def cycle_start_node(root):
    if root is None:
        return
    node_set = set()
    node_set.add(root)
    node_ptr = root
    while node_ptr != None:
        if node_ptr.next in node_set:
            return node_ptr.next
        node_set.add(node_ptr.next)
        node_ptr = node_ptr.next

def length_of_ll_with_cycle(root):
    if root is None:
        return
    node_set = set()
    node_set.add(root)
    len_of_ll = 1
    node_ptr = root
    while node_ptr != None:
        if node_ptr.next in node_set:
            return len_of_ll
        len_of_ll += 1
        node_set.add(node_ptr.next)
        node_ptr = node_ptr.next


if __name__=="__main__":

    n = get_linkedlist()
    n = get_ll_size1()
    node = cycle_start_node(n)
    print node.val #30
    print length_of_ll_with_cycle(n)