
"""
INPUT:[-2, -3, 4, -1, -2, 1, 5, -3]
INIT:[-2]
     [-2,max(-2+-3, -3)]
     [-2, max(-5,-3)]
     [-2, -3]
     [-2, -3, max(-3+4, 4)]
     [-2,-3,4]
     [-2,-3,4, max(4+-1, -1)]
     [-2,-3,4,3]
     [-2,-3,4,3, max(3+-2, -2)]
     [-2,-3,4,3,1]
     [-2,-3,4,3,1,max(1+1, 1)]
     [-2,-3,4,3,1,2]
     [-2,-3,4,3,1,2, max(2+5, 5)]
     [-2,-3,4,3,1,2,7]
     [-2,-3,4,3,1,2,7, max(7+-3,-3)]
     [-2,-3,4,3,1,2,7,4]
                    --
    Max Contiguous Subarray Sum: 7

    We need to create a new array with below logic.
    Should we include the element at position i?
    Only if sum of all elements till i-1 + A[i] > A[i] else
    the value at position i will be A[i]

    result[i] = max(result[i-i]+A[i], A[i])

"""
def largest_subarray_sum(A):
    max_elem = -1
    result_arr = []
    result_arr.append(A[0])
    for i in range(1, len(A)):
        local_max = max(result_arr[i-1]+A[i], A[i])
        result_arr.append(local_max)
        if local_max > max_elem:
            max_elem = local_max
    return max_elem


if __name__=="__main__":
    d = [-2,-3,4,-1,-2,1,5,-3]
    print largest_subarray_sum(d)