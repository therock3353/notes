'''
https://leetcode.com/explore/learn/card/binary-search/125/template-i/938/

Search Condition can be determined without comparing to the element's neighbors (or use specific elements around it)
No post-processing required because at each step, you are checking to see if the element has been found. If you reach the end, then you know the element is not found

Initial Condition: left = 0, right = length-1
Termination: left > right
Searching Left: right = mid-1
Searching Right: left = mid+1

'''

def binary_search(A, x):
    l = 0
    r = len(A)-1
    while l <= r:
        mid_pt = (l+r)/2
        if x == A[mid_pt]:
            return x
        elif x > A[mid_pt]:
            l = mid_pt + 1
        else:
            r = mid_pt - 1
    return -1
