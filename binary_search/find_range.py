
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