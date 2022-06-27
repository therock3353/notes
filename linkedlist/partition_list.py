"""
86. Partition List https://leetcode.com/problems/partition-list/

    10 -> 70 -> 40 -> 50 -> 10 -> 60 -> 50

            pivot around 50

    10 -> 40 -> 10 -> 50 -> 50 -> 70 -> 60

    Time Complexity: O(n)

    Solution:
       ---  10     <-  start_head
       |    |
       |    70 --   <- end_head
       |    |    |
       |--->40   |  <- start_ptr
            |    |
            50 --|--- <- middle head
            |    |  |
            10   |  |
            |    |  |
            60 <-   |
            |       |
            50 <----|


        start_head --> ....start_ptr->middle_head -> ... -> middle ptr->end_head -> ... ->end_ptr

"""
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def get_linkedlist():
    n1 = ListNode(10)
    n2 = ListNode(70)
    n3 = ListNode(40)
    n4 = ListNode(50)
    n5 = ListNode(10)
    n6 = ListNode(60)
    n7 = ListNode(50)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n7
    return n1

def print_nodes(head):
    n = head
    out = []
    while n != None:
        out.append(str(n.val))
        n = n.next
    return "->".join(out)


def partition_list(head, pivot):
    if head is None:
        return
    if head.next is None:
        return head
    start_head = None
    middle_head = None
    end_head = None
    start_ptr = None
    middle_ptr = None
    end_ptr = None
    node = head
    while node != None:
        if node.val < pivot:
            if start_head is None:
                start_head = node
                start_ptr = start_head
            else:
                start_ptr.next = node
                start_ptr = start_ptr.next
        elif node.val == pivot:
            if middle_head is None:
                middle_head = node
                middle_ptr = middle_head
            else:
                middle_ptr.next = node
                middle_ptr = middle_ptr.next
        else:
            if end_head is None:
                end_head = node
                end_ptr = end_head
            else:
                end_ptr.next = node
                end_ptr = end_ptr.next

        node = node.next
    start_ptr.next = middle_head
    middle_ptr.next = end_head
    end_ptr.next = None
    return start_head


if __name__=="__main__":
    ll = get_linkedlist()
    lst = partition_list(ll, 50)
    print print_nodes(lst)