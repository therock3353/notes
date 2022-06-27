"""
83. Remove Duplicates from Sorted List (linkedlist)
    https://leetcode.com/problems/remove-duplicates-from-sorted-list/

    Time Complexity: O(n)

"""
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def get_linkedlist():
    n1 = ListNode("10")
    n2 = ListNode("10")
    n3 = ListNode("10")
    n4 = ListNode("20")
    n5 = ListNode("40")
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


def remove_duplicates(head):
    if head is None:
        return
    if head.next is None:
        return head
    uniq_node_ptr_head = head
    uniq_node_ptr = head
    node_ptr = head.next
    while node_ptr != None:
        if uniq_node_ptr.val == node_ptr.val:
            while node_ptr != None and uniq_node_ptr.val == node_ptr.val:
                node_ptr = node_ptr.next
            uniq_node_ptr.next = node_ptr
        uniq_node_ptr = uniq_node_ptr.next
        if node_ptr != None:
            node_ptr = node_ptr.next

    return uniq_node_ptr_head

if __name__=="__main__":
    ll = get_linkedlist()
    lst = remove_duplicates(ll)
    print print_nodes(lst)