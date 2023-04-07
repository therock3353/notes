"""
129. Sum Root to Leaf Numbers

"""
def calculate_path_sum(node, path_sum, total):
    if node.left is None and node.right is None:
        path_sum += 10 * path_sum + node.val
        total += path_sum
        return total
    path_sum += 10*path_sum + node.val
    if node.left is not None:
        total = calculate_path_sum(node.left, path_sum, total)
    if node.right is not None:
        total = calculate_path_sum(node.right, path_sum, total)
    return total

def sum_root_to_leaf(root):
    if not root:
        return 0


if __name__=="__main__":
    n = get_tree()
    print sum_root_to_leaf(n)