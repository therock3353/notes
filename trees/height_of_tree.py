class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def generate_binary_tree():
    """
                        50
            30                      80
                40          70          90
            35      45           75
                              73
    """
    root = Node(50)
    n1 = Node(30)
    n2 = Node(40)
    n3 = Node(35)
    n4 = Node(45)
    n5 = Node(80)
    n6 = Node(70)
    n7 = Node(90)
    n8 = Node(75)
    n9 = Node(73)
    root.left = n1
    root.right = n5
    n1.right = n2
    n2.left = n3
    n2.right = n4
    n5.left = n6
    n5.right = n7
    n6.right = n8
    n8.left = n9
    return root


class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.children = []


def generate_tree():
    """
                                100
           40                    60                  120
    10        20      45                            102
        15       27                   101     105     107

    :return:
    """
    n = TreeNode(100)
    n1 = TreeNode(40)
    n2 = TreeNode(60)
    n3 = TreeNode(120)
    n.children = [n1, n2, n3]
    n4 = TreeNode(10)
    n5 = TreeNode(20)
    n6 = TreeNode(45)
    n1.children = [n4, n5, n6]
    n7 = TreeNode(15)
    n8 = TreeNode(27)
    n5.children = [n7, n8]
    n9 = TreeNode(102)
    n3.children = [n9]
    n10 = TreeNode(101)
    n11 = TreeNode(105)
    n12 = TreeNode(107)
    n9.children = [n10, n11, n12]
    return n

def post_order(node):
    if not node:
        return 0

    left_height = post_order(node.left)
    right_height = post_order(node.right)
    height = max(left_height, right_height) + 1
    return height


def height_binary_tree(root):
    if not root:
        return 0
    return post_order(root) - 1


def post_order_tree(node):
    if not node:
        return 0
    height = 0
    for child in node.children:
        child_height = post_order_tree(child)
        height = max(height, child_height)
    height += 1
    return height


def tree_height(root):
    if not root:
        return 0
    return post_order_tree(root) - 1


if __name__ == "__main__":
    root = generate_binary_tree()
    print height_binary_tree(root)
    root = generate_tree()
    print tree_height(root)
