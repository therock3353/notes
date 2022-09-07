"""
    93. Restore IP addresses https://leetcode.com/problems/restore-ip-addresses/

    There are 3 dots that need to be placed.
    Example: 1232170 here the 1st dot can be placed.
    1.232170 or 12.32170 or 123.2170
    for each of these cases:
        the next dot can be placed 1, 2 or 3 places after the 1st dot.
        It can be placed only after 1,2 or 3 places because the max subnet can be 255.
                        1.232170                                12.32170
                            |                                       |
                -------------------------               ----------------------------
            1.2.32170   1.23.2170   1.232.170           12.3.2170   12.32.170      12.321.70
                                                                                      (x)
    1.2.3.2170  1.2.32.170
          (x)

    3 dots can be placed with 3 possibilities (0th index, 1st index, 2nd index):
    O(n) = 3^3 = 9

"""

def is_valid_subsec(partial_num):
    if partial_num is None or partial_num == "":
        return False
    if partial_num.startswith("0") and len(partial_num) > 1:
        return False
    if 0 <= int(partial_num) <= 255:
        return True
    else:
        return False

def recur(num, k, result, results):
    if num is None:
        return
    if k == 0:
        if is_valid_subsec(num) is True:
            result.append(num)
            results.append(".".join(result))
        return

    for i in range(len(num)):
        selected = num[:i+1]
        remaining = num[i+1:]
        if is_valid_subsec(selected) is True:
            recur(remaining, k-1, result+[selected], results)


def restore_ip_addr(num):
    if not num:
        return []
    results = []
    recur(num, 3, [], results)
    return results

num = "0000"
print restore_ip_addr(num)