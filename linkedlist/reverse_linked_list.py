"""
Leetcode 206: https://leetcode.com/problems/reverse-linked-list/

"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def get_linkedlist():
    n1 = ListNode(10)
    n2 = ListNode(20)
    n3 = ListNode(30)
    n4 = ListNode(40)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    return n1

def print_nodes(head):
    n = head
    out = []
    while n != None:
        out.append(str(n.val))
        n = n.next
    print("->".join(out))

def reverse1(head):
    next_node = head
    prev_node = None

    while next_node != None:
        p = ListNode(val=next_node.val)
        p.next = next_node.next
        next_node.next = prev_node
        prev_node = next_node
        next_node = p.next

    head = prev_node
    return head

def reverse2(head):
    if not head:
        return
    if head.next is None:
        return head

    prev = None
    curr = head
    next = head.next
    while next != None:
        curr.next = prev
        prev = curr
        curr = next
        next = next.next

    curr.next = prev
    head = curr
    return head

if __name__=="__main__":

    n = get_linkedlist()
    print_nodes(n)
    new_head = reverse1(n)
    print_nodes(new_head)
    n = get_linkedlist()
    print_nodes(n)
    new_head = reverse2(n)
    print_nodes(new_head)
