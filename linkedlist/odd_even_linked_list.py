"""
Leetcode 328: https://leetcode.com/problems/odd-even-linked-list/

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
    n.next = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    return n

def print_nodes(head):
    n = head
    out = []
    while n != None:
        out.append(str(n.val))
        n = n.next
    print "->".join(out)

class Solution(object):

    def oddEvenList(self, head):
        if head is None:
            return
        if head.next is None:
            return head

        odd_head = head
        odd = head
        even_head = head.next
        even = head.next
        n = head.next.next

        flag = True
        while n != None:
            if flag is True:
                flag = False
                odd.next = n
                odd = odd.next
            elif flag is False:
                flag = True
                even.next = n
                even = even.next
            n = n.next
        odd.next = even_head
        even.next = None

        return odd_head

if __name__=="__main__":

    l = get_linkedlist()
    new_head = Solution().oddEvenList(l)
    print_nodes(new_head)














# class Solution(object):
#
#     def oddEvenList(self, head):
#         if head is None:
#             return
#         if head.next is None:
#             return head
#
#         odd_head = head
#         even_head = head.next
#         odd_ptr = odd_head
#         even_ptr = even_head
#         head = head.next
#         head = head.next
#         index = 1
#         while head != None:
#             if index % 2 == 1:
#                 odd_ptr.next = head
#                 odd_ptr = odd_ptr.next
#             else:
#                 even_ptr.next = head
#                 even_ptr = even_ptr.next
#
#             head = head.next
#             index +=1
#
#         odd_ptr.next = even_head
