
"""

                [5, 4, 80, 60, 23, 6, 2, 1]
SPLIT PHASE     [5, 4, 80, 60][23, 6, 2, 1]
                [5, 4][80, 60][23, 6][2, 1]

MERGE PHASE     [4, 5][60, 80][6, 23][1, 2]
                [4, 5, 60, 80][1, 2, 6, 23]
                [1, 2, 4, 5, 6, 23, 60, 80]

Essentially merge sort has below 2 steps:
    a. Split the input array into half recursively unless array length is less than 2.
    This can be achived O(1) as we calculate the mid pt by arithmetic len(arr)/2 or (high+low)/2
    b. Merge the two individually sorted arrays into a single array. If two arrays are of length
    n/2 then the operational complexity of merging two n/2 arrays is n.

    worst case of merging:
        [1,3,5]
        [4,6,20]
        [1,3,4,5,6,20] => we had to do 5 comparisions here.

    Since there are log(n) times the merging happens and in each iteration we merge n elements O(n).
    The total complexity is nlog(n).
                            [5, 4, 80, 60, 23, 6, 2, 1]
                        -----------------------------                       |
                        |                            |                      |
                    [5, 4, 80, 60]              [23, 6, 2, 1]               |   merge n numbers => O(n)
                -----------------              -----------------            |           :
                |                |             |                |           |           :
            [5, 4]           [80, 60]       [23, 6]           [2, 1]        |   merge n numbers => O(n)

                                                                               We do this operation log(n) times. ==> nlog(n)

"""

def merge(first, second):
    result = []
    idx1, idx2 = 0, 0
    while idx1 < len(first) and idx2 < len(second):
        if first[idx1] >= second[idx2]:
            result.append(second[idx2])
            idx2 += 1
        elif first[idx1] < second[idx2]:
            result.append(first[idx1])
            idx1 += 1

    if idx1 < len(first):
        while idx1 < len(first):
            result.append(first[idx1])
            idx1 += 1
    elif idx2 < len(second):
        while idx2 < len(second):
            result.append(second[idx2])
            idx2 += 1
    return result

def divide(arr):
    if len(arr) <= 2:
        if len(arr) <= 1:
            return arr
        elif len(arr) == 2:
            if arr[0] > arr[1]:
                arr[0], arr[1] = arr[1], arr[0]
        return arr
    mid_pt = len(arr)/2  # -> [a, b, c, d] 4/2 = 2
                         #
                         # -> [a, b, c, d, e] 5/2 = 2
                         #
    first = divide(arr[:mid_pt])
    second = divide(arr[mid_pt:])
    result = merge(first, second)
    return result

def merge_sort(nums):
    if not nums:
        return nums
    return divide(nums)

# Best Case O(nlog(n))
# If array is already sorted, still merge sort will split the array and merge the array of length n, log(n) times.
# ----------------
# Worst Case O(nlog(n))
# -----------------
# Average Case O(nlog(n))
# ------------------

if __name__=="__main__":
    d = [10,4,5,2,8,18,9]
    print merge_sort(d)
    d = [100]
    print merge_sort(d)
    d = [88,1]
    print merge_sort(d)
    d = [-2, -90, 7, 1]
    print merge_sort(d)
