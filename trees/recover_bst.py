class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

'''
https://leetcode.com/problems/recover-binary-search-tree
    
                        20
                10             15
            5      30       25     35

        If you do inorder traversal for Binary Search Tree, you get a sorted array
        [5,10,30,20,25,15,35]
        Here the array is almost sorted, except for 2 points. We can sort the array and compare with original
        [5,10,30,20,25,15,35]
               |        |
        [5,10,15,20,25,30,35]
        These are the 2 elements out of order.
        But this requires additional space O(n) & sorting etc is extra.
        
        We can also do this more efficiently by inorder tree traversal.
        Tree traversal has 2 parts: 1. identify when curr node < prev node.
        2.store nodes a & b 
        
        (1) can be achieved as:
        def inorder(node, prev):
            if not node:
                return prev
            prev = inorder(node.left, prev)
            if prev:
                print("prev {}, curr {}".format(prev.val, curr.val))
            prev = inorder(node.right, node)
            return prev
            
        for (2):  
            representing tree as an array for explanation:
            [5, 10, 30, 20, 25, 15, 35]
            
            We don't know whether the first prev>curr fixes the tree or
            there are two such conditions.
                         10
                    5        15             Here if we swap 15 & 18 then it fixes the tree
                          18    25          so only once prev>curr it true
            -   -   -   -   -   -   -   - 
                        20
                10             15           But here we need to swap 30 & 15 so prev>curr is true 2 times.
            5      30       25     35       30>20 & 25>15
            
            let's say we store these nodes in a & b.
            [5,  10,  18,  15,  25]        [5,  10,  30,   20,  25,   15,  35]
                     prev  cur                       prev  cur  prev  cur
                       b    a                         b     a          b
            if prev > curr:
                a = curr
                if b is None:   #a is always updated to curr hence a=20 but in next iterations a becomes 15
                    b = prev    #but b is only updated once with higher value of prev
            

'''

def get_tree():
    n1 = TreeNode(20)
    n2 = TreeNode(10)
    n3 = TreeNode(5)
    n4 = TreeNode(30)
    n5 = TreeNode(15)
    n6 = TreeNode(25)
    n7 = TreeNode(35)
    n1.left = n2
    n1.right = n5
    n2.left = n3
    n2.right = n4
    n5.left = n6
    n5.right = n7
    return n1

class Solution(object):
    def inorder(self, node, prev, a, b):
        if not node:
            return (a,b,prev)
        res = self.inorder(node.left, prev, a, b)
        a = res[0]
        b = res[1]
        prev = res[2]
        if prev and node.val < prev.val:
            a = node
            if b is None:
                b = prev
            # print("prev: {}, curr {}".format(prev.val, node.val))
        res = self.inorder(node.right, node, a, b)
        a = res[0]
        b = res[1]
        prev = res[2]
        return (a,b,prev)

    def recoverTree(self, root):
        if not root:
            return
        res = self.inorder(root, None, None, None)
        print(res[0].val, res[1].val)
        a = res[0]
        b = res[1]
        a.val, b.val = b.val, a.val
        return root