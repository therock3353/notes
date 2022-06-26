"""
128 Longest Consecutive Sequence https://leetcode.com/problems/longest-consecutive-sequence/

        A = [100, 5, 9, 101, 4, 0, 3, 20, 25, 6, 8, 102, 7, 24]
        consecutive seq are: 100,101,102
                             3,4,5,6,7,8,9 <= longest

        Brute force: Sort array and check if A[i]+1 = A[i+1]
            O(nlog(n))
"""
def longest_conseq_seq_brute_force(A):
    if not A:
        return 0
    if len(A) == 1:
        return 1
    A.sort()
    longest_seq_len = 1
    curr_seq_len = 1
    i = 0
    while i < len(A)-2:
        if A[i+1] - A[i] == 1:
            curr_seq_len += 1
        else:
            if curr_seq_len > longest_seq_len:
                longest_seq_len = curr_seq_len
            curr_seq_len = 1
        i += 1
    if curr_seq_len > longest_seq_len:
        longest_seq_len = curr_seq_len
    return longest_seq_len

"""
    To do the problem in O(n) time complexity, store all elements in a set.
    for each element in A:
        next_elem = elem + 1
        while next element in set:
            
        prev_elem = elem - 1
        while prev element in set:
        
    You iterate over the array A twice so O(n) = 2n ~= n
    Worst case is also O(n)
"""
def longest_conseq_seq(A):
    if not A:
        return 0
    if len(A) == 1:
        return 1
    numbers = set()
    for num in A:
        numbers.add(num)
    longest_seq_len = 1
    curr_seq_len = 1
    for num in A:
        if num in numbers:
            next_num = num + 1
            while next_num in numbers:
                numbers.remove(next_num)
                next_num += 1
                curr_seq_len += 1
            prev_num = num - 1
            while prev_num in numbers:
                numbers.remove(prev_num)
                prev_num -= 1
                curr_seq_len += 1
            if curr_seq_len > longest_seq_len:
                longest_seq_len = curr_seq_len
            curr_seq_len = 1
    return longest_seq_len

if __name__=="__main__":

    A = [100, 5, 9, 101, 4, 0, 3, 20, 25, 6, 8, 102, 7, 24]
    print(longest_conseq_seq(A))
    print longest_conseq_seq_brute_force(A)