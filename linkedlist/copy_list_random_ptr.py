"""
Leetcode 138: https://leetcode.com/problems/copy-list-with-random-pointer/

"""
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        self.random = None

def get_linkedlist():
    n1 = ListNode(10)
    n2 = ListNode(20)
    n3 = ListNode(30)
    n4 = ListNode(40)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n1.random = n4
    n2.random = n2
    n3.random = n1
    n4.random = n1
    return n1

def print_nodes(head):
    n = head
    out = []
    while n != None:
        out.append(str(n.val))
        n = n.next
    print("->".join(out))
    n = head
    out = []
    while n != None:
        if n.random is not None:
            out.append(str(n.random.val))
        else:
            out.append("None")
        n = n.next
    print("->".join(out))

def copy_random_list(head):
    if not head:
        return
    if head.next == None:
        return head

    nodes = {}
    n = head
    new_head = None
    new_n = None
    cntr = 0
    while n != None:
        p = ListNode(n.val)
        if new_head is None:
            new_head = p
            new_n = new_head
        else:
            new_n.next = p
            new_n = new_n.next
        nodes[str(cntr)+str(p.val)] = p
        n = n.next
        cntr += 1

    n = head
    new_n = new_head
    cntr = 0
    while n != None and new_n != None:
        if n.random is not None:
            new_next_random = nodes.get(str(cntr)+str(n.random.val))
        else:
            new_next_random = None
        new_n.random = new_next_random
        n = n.next
        new_n = new_n.next
        cntr += 1
    return new_head

if __name__=="__main__":
    ll = get_linkedlist()
    print_nodes(ll)
    new_lst = copy_random_list(ll)
    print_nodes(new_lst)