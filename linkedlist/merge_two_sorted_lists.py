"""
21. Merge Two Sorted Lists https://leetcode.com/problems/merge-two-sorted-lists/


"""
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def get_linkedlist():
    n1 = ListNode("10")
    n2 = ListNode("30")
    n3 = ListNode("80")
    n4 = ListNode("90")
    n5 = ListNode("150")
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    return n1

def get_linkedlist2():
    n1 = ListNode("5")
    n2 = ListNode("50")
    n3 = ListNode("160")
    n1.next = n2
    n2.next = n3
    return n1


def print_nodes(head):
    n = head
    out = []
    while n != None:
        out.append(str(n.val))
        n = n.next
    return "->".join(out)


def merge_lists(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1
    result_head = None
    result = None
    while l1 != None and l2 != None:
        if int(l1.val) < int(l2.val):
            if result_head is None:
                result_head = l1
                result = result_head
            else:
                result.next = l1
                result = result.next
            l1 = l1.next
        else:
            if result_head is None:
                result_head = l2
                result = result_head
            else:
                result.next = l2
                result = result.next
            l2 = l2.next

    if l1 is None and l2 is not None:
        while l2 != None:
            result.next = l2
            result = result.next
            l2 = l2.next

    if l2 is None and l1 is not None:
        while l1 != None:
            result.next = l1
            result = result.next
            l1 = l1.next

    return result_head


if __name__=="__main__":
    l1 = get_linkedlist()
    l2 = get_linkedlist2()
    lst = merge_lists(l1, l2)
    print print_nodes(lst)