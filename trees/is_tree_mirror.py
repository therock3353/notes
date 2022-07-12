"""
EPI 9.2 Check if Tree's left half is mirror image of right half

            10
        5       5
    6              6
        8       8
"""
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def generate_tree():
    n = Node(10)
    n1 = Node(5)
    n2 = Node(5)
    n.left = n1
    n.right = n2
    n3 = Node(6)
    n4 = Node(6)
    n1.left = n3
    n2.right = n4
    n5 = Node(8)
    n6 = Node(8)
    n3.right = n5
    n4.left = n6
    return n

def is_mirror_image(t1, t2):
    if t1 is None and t2 is None:
        return True
    if (t1 is None and t2 is not None) or (t2 is None and t1 is not None):
        return False
    if t1.value != t2.value:
        return False
    left_subtree_mirror = is_mirror_image(t1.left, t2.right)
    right_subtree_mirror = is_mirror_image(t1.right, t2.left)
    return left_subtree_mirror and right_subtree_mirror

def is_tree_mirror(root):
    if not root:
        return False
    return is_mirror_image(root.left, root.right)

if __name__=="__main__":
    root = generate_tree()
    print is_tree_mirror(root)