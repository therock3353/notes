"""
    [4,8,3,5]
    for i in 1->n:
        for j in 1->n:
            compare A[j] to A[j+1]

1st pass:
    i =0, j = 0, j+1 = 1
        compare nums[j=0] to nums[j=1] & move the larger element to j=1
    [4,8,3,5]
    i =0, j = 1, j+1 = 2
        compare nums[j=1] to nums[j=2] & move the larger element to j=2
    [4, 3, 8, 5]
        ^--^
    i =0, j = 2, j+1 = 3
        compare nums[j=2] to nums[j=3] & move the larger element to j=3
    [4, 3, 5, 8]
           ^--^
    At the end of one i pass, largest element "bubbles" at the rightmost position
After 2nd pass:
    i =1, j = 0, j+1 = 1
        compare nums[j=0] to nums[j=1] & move the larger element to j=1
    [3, 4, 5, 8]
    ^--^
    i =1, j = 1, j+1 = 2
        compare nums[j=1] to nums[j=2] & move the larger element to j=2
    [3, 4, 5, 8]
    i =1, j = 2, j+1 = 3
        compare nums[j=2] to nums[j=3] & move the larger element to j=3
    [3, 4, 5, 8]
    At the end of 2nd pass, the 2nd largest element 5, "bubbles" at the right position
After 3rd pass:
    In this specific example, 3rd pass is not required.
"""
def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(len(nums)-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

# Best Case O(n) ** check below
# ----------------
# i from 1 --> n
#   j from 1 --> n
# Worst Case O(n^2):
# -----------------
# Average Case O(n^2):
# ------------------
# Doesn't matter best, worst case, the bubble sort always gives O(n^2)
# because we don't really know if elements are sorted or not.

# We can improve the operational complexity by optimization.
# We can track if there are any swap operations performed or not.
# If no swap operations are performed then no need to continue.
# The Best case becomes O(n) i.e if all numbers are already sorted
# then we just have to go through the loop only once to know that there
# is no swap hence no need to continue further.

def bubble_sort_optimized(nums):
    swapped = True
    for i in range(len(nums)):
        if swapped is False:
            break
        swapped = False
        for j in range(len(nums)-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swapped = True
    return nums


if __name__=="__main__":
    d = [4, 8, 3, 5]
    print bubble_sort(d)
    print bubble_sort_optimized(d)