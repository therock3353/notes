'''
https://leetcode.com/problems/max-consecutive-ones-iii/description/

You are given seq = [1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1] & k = 2
you can switch any 0 to 1, max k times. This is a sliding window problem.

    for end in range(len(data)):
        3 cases here:
        if data[end] == 1:
            great, we can expand the window
        elif k > 0:
            now we are processing a 0 but since k > 0,
            we can expand the window. But need to decrement k by 1
        else:
            we are processing a 0 and out of k ie k == 0.
            now we must shrink the window so that it becomes valid again.
            while k == 0:
                if data[start] == 0:
                    k += 1
                start += 1

'''

def maxConsecutiveOnce(data, k):
    lenOfSeq = 0
    start = 0
    for end in range(len(data)):
        if data[end] == 1:
            lenOfSeq = max(lenOfSeq, end-start+1)
        elif k > 0:
            k -= 1
            lenOfSeq = max(lenOfSeq, end-start+1)
        else:
            while k <= 0:
                if data[start] == 0:
                    k += 1
                start += 1
            k -= 1
            lenOfSeq = max(lenOfSeq, end-start+1)

    return lenOfSeq

seq = [1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1]
print(maxConsecutiveOnce(seq, 2))