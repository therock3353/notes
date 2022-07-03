"""
Leetcode 19: https://leetcode.com/problems/remove-nth-node-from-end-of-list/


"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    """
        n1 -> n2 -> n3 -> n4 -> n5 -> None

    1)  n=2
        n1 -> n2 -> n3 -> n5 -> None

    2) n = 4
        n1 -> n3 -> n4 -> n5 -> None

    There are two possibilities:
        1. nth node from tail is head:
            head = head.next
            n1 -> n2 -> n3 -> None (n=3) then result => n2-> n3 -> None
            corner cases:
                n1 -> n2 -> None (n=1) then result => n1 -> None
                n1 -> n2 -> None (n=2) then result => n2 -> None
        2. nth node is in-between somewhere
                get to (n-1)th node.
                node.next = node.next.next

    """

    def removeNthFromEnd(self, head, n):
        if not n or head is None:
            return head

        node = head
        len_of_ll = 0
        while node != None:
            len_of_ll += 1
            node = node.next

        prev_node_pos = len_of_ll - n
        if prev_node_pos <= 0:
            head = head.next
            return head
        curr_ptr = head
        while prev_node_pos > 1:
            prev_node_pos -= 1
            curr_ptr = curr_ptr.next

        curr_ptr.next = curr_ptr.next.next
        return head


if __name__=="__main__":
    pass
