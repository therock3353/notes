"""
Leetcode 2 https://leetcode.com/problems/add-two-numbers/
    The 2 numbers represented by linked-list are say: 283 and 9780 (283+9780 = 10063)
    The numbers are already provided as reversed linked list

    num1        3 -> 8 -> 2
    num2        0 -> 8 -> 7 -> 9

            3   +    0  + remaininder(0) = 3
            |        |
            8   +    8  + remaininder(0) = 6
            |        |
            2   +    7  + remaininder(1) = 0
                     |
                     9  + remaininder(1) = 0

                        + remainder(1)   = 1
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = None
        result_head = None
        remainder = 0
        if l1 is None and l2 is None:
            return result_head
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        while l1 != None and l2 != None:
            res = l1.val + l2.val + remainder
            if res >= 10:
                remainder = 1
                res = res - 10
            else:
                remainder = 0
            if result is None:
                result = ListNode(res)
                result_head = result
            else:
                result.next = ListNode(res)
                result = result.next
            l1 = l1.next
            l2 = l2.next

        if l1 is None and l2 != None:
            while l2 != None:
                res = l2.val + remainder
                if res >= 10:
                    remainder = 1
                    res = res - 10
                else:
                    remainder = 0
                result.next = ListNode(res)
                result = result.next
                l2 = l2.next
        elif l1 != None and l2 is None:
            while l1 != None:
                res = l1.val + remainder
                if res >= 10:
                    remainder = 1
                    res = res - 10
                else:
                    remainder = 0
                result.next = ListNode(res)
                result = result.next
                l1 = l1.next
        #
        # Often I will forget this point.
        # if the two lists are like this
        #   7 -> 0 -> 8
        #   6 -> 5 -> 2 -> 9
        #  then the last reminder will be 10 so need to add both the digits
        #
        if remainder != 0:
            result.next = ListNode(remainder)

        return result_head

if __name__=="__main__":