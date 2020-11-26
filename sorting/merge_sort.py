
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

if __name__=="__main__":
    d = [10,4,5,2,8,18,9]
    print merge_sort(d)
    d = [100]
    print merge_sort(d)
    d = [88,1]
    print merge_sort(d)
    d = [-2, -90, 7, 1]
    print merge_sort(d)
