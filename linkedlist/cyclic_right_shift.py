"""
    Cyclic right shift of linkedlist

    10 -> 20 -> 30 -> 40 -> 50 -> 60

        right shift by 2

    50 -> 60 -> 10 -> 20 -> 30 -> 40

    Time complexity O(n)

    Solution:
    10 -> 20 -> 30 -> 40 -> 50 -> 60
    ptr         fast
          ptr         fast
                ptr         fast
                      ptr         fast

    new_head = ptr.next (50 is the next head)
    ptr.next = None     (40 points to None)
    fwd.next = head     (60 points to original head)

    10 -> 20 -> 30 -> 40 ->None
     ^                           50 -> 60 --
     |                          head       |
     |                                     |
     |-------------------------------------|

"""
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def get_linkedlist():
    n1 = ListNode("10")
    n2 = ListNode("20")
    n3 = ListNode("30")
    n4 = ListNode("40")
    n5 = ListNode("50")
    n6 = ListNode("60")

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    return n1

def print_nodes(head):
    n = head
    out = []
    while n != None:
        out.append(str(n.val))
        n = n.next
    return "->".join(out)

def cyclic_right_shift(head, k):
    if not head or k == 0:
        return
    if head.next is None:
        return head
    ll_len = 0
    node = head
    fwd_ptr = head
    while node != None:
        ll_len += 1
        node = node.next
    k = k % ll_len
    i = 0
    while i < k:
        fwd_ptr = fwd_ptr.next
        i += 1
    node = head
    while fwd_ptr.next != None:
        fwd_ptr = fwd_ptr.next
        node = node.next
    new_head = node.next
    fwd_ptr.next = head
    node.next = None
    return new_head


if __name__=="__main__":
    ll = get_linkedlist()
    print print_nodes((ll))
    lst = cyclic_right_shift(ll, 3)
    print print_nodes(lst)