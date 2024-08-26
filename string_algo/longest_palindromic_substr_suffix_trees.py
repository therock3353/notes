class SuffixNode(object):
    def __init__(self):
        self.children = {}
        self.end_of_word = None

def is_palindrom(s):
    left = 0
    right = len(s)-1
    while left < right:
        if s[left] != s[right]:
            return False
        left +=1
        right -=1
    return True

def print_suffix_tree(key, node, result, results):
    if not node.children:
        result = result + key
        results.append(result)
        return

    for c in node.children.keys():
        if node.children.get(c) and node.children.get(c).children:
            result = result + c
        print_suffix_tree(c, node.children.get(c), result, results=results)
        result = result[1:]


def create_suffix_tree(root, suffix):
    node = root
    for char in suffix:
        if node.children.get(char, None) is None:
            node.children[char] = SuffixNode()
        node = node.children.get(char, None)

    node.end_of_word = True
    return root

def generate_all_suffixes(str):
    all_suffixes = []
    st_pt = len(str)-1
    end_pt = len(str)

    while st_pt >= 0:
        suffix = str[st_pt: end_pt]
        all_suffixes.append(suffix)
        st_pt -=1
    print " all_suffixes of s {} : {}".format(str, all_suffixes)
    return all_suffixes

def longest_palindromic_substr(s):
    if not s:
        return ""
    if len(s) == 1:
        return s
    reversed_s = s[::-1]
    s_suffixes = generate_all_suffixes(s)
    reversed_s_suffixes = generate_all_suffixes(reversed_s)
    root = SuffixNode()
    for suffix in s_suffixes:
        create_suffix_tree(root, suffix)
        results = []
        result = ""
        print_suffix_tree(None, root, result, results)
        print results
    # results = []
    # result = []
    # print_suffix_tree(None, root, [], [])
    # print results

if __name__=="__main__":
    s = "pabbaqm"
    print longest_palindromic_substr(s)