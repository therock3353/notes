"""
3. Longest Substring Without Repeating Characters https://leetcode.com/problems/longest-substring-without-repeating-characters/

    a, b, c, d, m, q, c, m, n, a, d, x
    | len = 1
       | len = 2
            ...
                      | len = 6

    Starting at a till 6th index c, we have all uniq characters. so len of uniq char so far = 6
    Now since c is the repeated char, there is no point from starting from any char behind c (3rd index)
    as you will get the same result. Hence start at the next index to c's 1st occurance ie d at index 4.

    next seq: d, m, q, c, [m] since m is repeated seq, now start at q.

"""

def longest_substr_wo_repeating_char(A):
    if not A:
        return 0
    if len(A) == 1:
        return 1
    index = 0
    uniq_char_index_map = {}
    curr_substr_len = 0
    longest_substr_len = 0
    while index < len(A):
        if A[index] not in uniq_char_index_map:
            uniq_char_index_map[A[index]] = index
            curr_substr_len += 1
        else:
            index = uniq_char_index_map[A[index]]
            if curr_substr_len > longest_substr_len:
                longest_substr_len = curr_substr_len
            uniq_char_index_map = {}
            curr_substr_len = 0
        index += 1

    if curr_substr_len > longest_substr_len:
        longest_substr_len = curr_substr_len
    return longest_substr_len

if __name__=="__main__":
    #s = "abcdmqcmmaddx"
    s = "abcabcbb"
    print longest_substr_wo_repeating_char(s)
