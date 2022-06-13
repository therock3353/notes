"""
Delete a node from linkedlist

                    10 -> 20 -> 30 -> 40 -> 50 -> None
     DELETE 40
                    |
                    n
                    n = n.next
                           |
                           n
                           n = n.next
                                |
                                n
                                n.next = delete_node
                                n.next = n.next.next

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
    n5 = ListNode(50)
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
    print("->".join(out))

def is_equal(node1, node2):
    if node1 is None and node2 is None:
        return True
    if node1 is None and node2 is not None:
        return False
    if node1 is not None and node2 is None:
        return False
    if node1.val == node2.val and node1.next == node2.next:
        return True
    return False

def delete_node(root, node):
    if root is None or node is None:
        return
    if root == node:
        return root.next
    n = root
    while n != None:
        if n.next == node:
            n.next = n.next.next
            break
        n = n.next
    return root

if __name__=="__main__":

    head = get_linkedlist()
    n = head
    for i in range(3):
        n = n.next
    print "deleting node {}".format(n.val)
    head = delete_node(head, n)
    print_nodes(head)