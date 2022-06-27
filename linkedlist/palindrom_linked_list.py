"""
Leetcode 234: https://leetcode.com/problems/palindrome-linked-list/

    Time Complexity:
        reverse O(n) + Compare O(n) = O(n)
    Space Complexity:
        need additional space for the new reversed ll O(n)
"""
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def get_linkedlist():
    n1 = ListNode("A")
    n2 = ListNode("B")
    n3 = ListNode("B")
    n4 = ListNode("B")
    n5 = ListNode("A")
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    return n1

def print_nodes(head):
    n = head
    out = []
    while n != None:
        out.append(str(n.val))
        n = n.next
    return "->".join(out)

def reverse(head):
    if not head:
        return
    if head.next is None:
        return ListNode(head.val)
    n = head
    prev = None
    curr = None
    while n != None:
        curr = ListNode(n.val)
        curr.next = prev
        prev = curr
        n = n.next
    return curr

def is_palindrom(head):
    if not head:
        return False
    if head.next is None:
        return True
    ll = head
    reversed_ll = reverse(head)
    while ll != None and reversed_ll != None:
        if ll.val != reversed_ll.val:
            return False
        ll = ll.next
        reversed_ll = reversed_ll.next
    return True

if __name__=="__main__":

    n = get_linkedlist()
    print is_palindrom(n)