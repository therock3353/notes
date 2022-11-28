
# Variant
#   If the array has multiple duplicates then find the left and right boundry.
#     d = [0,0,1,1,1,1,1,1,1,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,4,4]
#     x = 2
# 2 has left boundry of 9 index and right boundry of 11th index.
# One way to solve this is using binary search find any occurance of 9 and then do a linear comparision
# to left and right.

def find_boundry_linear(A, target):
    left = 0
    right = len(A)-1
    left_boundry, right_boundry = -1, -1
    while left<=right:
        mid_pt = (left+right)/2
        if A[mid_pt] == target:
            index = mid_pt
            while index>=0 and A[index] == A[index-1]:
                index-=1
            left_boundry = index
            index = mid_pt
            while index < len(A) and A[index] == A[index+1]:
                index+=1
            right_boundry = index
            return [left_boundry, right_boundry]
        elif A[mid_pt] > target:
            right = right-1
        else:
            left = left+1

    return [left_boundry, right_boundry]

# here we are searching for 2 and when we find 2 O(log(n)) then we go left N1 steps and right N2 steps.
# So effectively the complexity is O(log(n) + (N1+N2)). If N1 or N2 is really large. (example: array of 1000 elements
# with 990 same elements that you are searching for, the complexity becomes linear.
#
# We can also use binary search (with minor change in implementation) to search for boundries using O(log(n))

def find_boundry(A, target):
    left1 = 0
    right1 = len(A)-1
    left_boundry = -1
    while left1<=right1:
        mid_pt = (left1+right1)/2
        if A[mid_pt] >= target:
            right1 = mid_pt-1
        else:
            left1 = mid_pt + 1
    left2 = 0
    right2 = len(A)-1
    right_boundry = -1
    while left2<=right2:
        mid_pt = (left2+right2)/2
        if A[mid_pt] <= target:
            left2 = mid_pt+1
        else:
            right2 = mid_pt-1

    if right2>=left1:
        left_boundry = left1
        right_boundry = right2
    return [left_boundry, right_boundry]

# Below is alternative implementation of the same concept.
# You have left and right ptr. left = 0 and right = len(A)-1
# To find left boundary, you take right pointer and try to place it towards left-most element
# To find right boundary, you take left ptr and try to place it towards right-most element
#   left boundary:
#       [10, 20, 20, 20, 20, 20, 30]    target = 20
#        l           m          <- r
#        l         <-r
#        l    r
#   There are two cases:
#       [10, 20, 20 ..]                    [10, 20, 20, ...]
#        l    r                                 l    r
#                   if (right - left) == 1:
#                       if A[left] == target:           Since we are looking for left boundary, check left first
#                           left_boundary = left
#                       elif A[right] == target:
#                           left_boundary = right
#
#   Same applies for right boundary as well.
#
#   right boundary:
#       [10, 20, 20, 20, 20, 20, 30]    target = 20
#        l->         m            r
#                    l            r
#                         l       r
#   There are two cases:
#       [...20, 20, 30]                    [..., 20, 20, 30]
#            l   r                                    l   r
#                   if (right - left) == 1:
#                       if A[right] == target:           Since we are looking for right boundary, check right first
#                           right_boundary = right
#                       elif A[left] == target:
#                           left_boundary = left
#
def find_boundry_alt(A, target):
    if not A or target is None:
        return -1
    left = 0
    right = len(A)-1
    result = []
    while left <= right:
        mid = (left+right)/2
        if (right - left) == 1 or (left == right):
            if A[left] == target:
                result.append(left)
            elif A[right] == target:
                result.append(right)
            break
        if target > A[mid]:
            left = mid + 1
        elif target < A[mid]:
            right = mid - 1
        else:
            right = mid
    if not result:
        result.extend([-1, -1])
        return result
    left = result[0]
    right = len(A) - 1
    while left <= right:
        mid = (left+right)/2
        if (right - left) == 1 or (left == right):
            if A[right] == target:
                result.append(right)
            elif A[left] == target:
                result.append(left)
            break
        if target > A[mid]:
            left = mid + 1
        elif target < A[mid]:
            right = mid - 1
        else:
            left = mid
    return result

# A = [1,1,1,1,2,3]
# target = 1
# print find_boundry_alt(A, target)
# A = [1,2,3,4,6,7,8,9,10]
# target = 5
# print find_boundry_alt(A, target)
# A = [5,7,8,10,12,14,16]
# target = 7
# print find_boundry_alt(A, target)
A = [5, 10]
target = 8
print find_boundry_alt(A, target)

