"""
    https://www.youtube.com/watch?v=fV-TF4OvZpk
    https://www.youtube.com/watch?v=odrfUCS9sQk
    https://www.youtube.com/watch?v=CE2b_-XfVDk

    A = [2, 10, 1, -4, 5, 6, 2, 18]

    dp = [1,1,1,1,1,1,1,1] #dp arrary is initialized to 1 because min length of sub-sequence is 1
            i.e individual elements.

    dp[0,0] = 1
    dp[0,1] = 2 [2, 10] Since 10 is greater than 2, the length of longest sub-sequence at ends at 10 is
                    length of longest sub-sequence that ends at 2 + 1
    dp[0,2] = 1
                dp[1,2,1,1,1,1,1,1]
                Since A[2] = 1 which is smaller than A[0] and A[1], the length of longest sub-sequence that ends at A[2] is 1
    dp[0,3] = 1
                dp[1,2,1,1,1,1,1,1]
                Since A[3] = -4 which is smaller than A[0], A[1] and A[2], the length of longest sub-sequence that ends at A[3] is 1
    dp[0,4] = 2
                A[4] = 5
                A[4] > A[0] Hence A[4] can be part of sub-sequence that ends at A[0]
                        also currently dp is [1,2,1,1,1,1,1,1] where A[4] = 1
                        so if the sub-sequence is [2,5] then length becomes 2 hence dp [1,2,1,1,"2",1,1,1]

                A[4] < A[1] Hence A[4] cannot be part of sub-sequence that ends at A[1]. We need increasing sub-sequence.
                        dp = [1,2,1,1,"2",1,1,1]
                A[4] > A[2] Hence A[4] can be part of sub-sequence that ends at A[2]
                        also currently dp is [1,2,1,1,"2",1,1,1] where dp[4] = 2
                        so if the sub-sequence is [1,5] then length becomes 2 since the length is already 2 we can ignore.
                A[4] > A[3] Hence A[4] can be part of sub-sequence that ends at A[3]
                        also currently dp is [1,2,1,1,"2",1,1,1] where dp[4] = 2
                        so if the sub-sequence is [-4,5] then length becomes 2 since the length is already 2 we can ignore.

    dp[0,5] = 3
                A[5] = 6
                A[5] > A[0] Hence A[5] can be part of sub-sequence that ends at A[0]
                        also currently dp is [1,2,1,1,2,"1",1,1] where A[5] = 1
                        so if the sub-sequence is [2,6] then length becomes 2 hence dp [1,2,1,1,2,"2",1,1]
                A[5] < A[1] Hence A[5] cannot be part of sub-sequence that ends at A[1]. We need increasing sub-sequence.
                        dp = [1,2,1,1,2,"2",1,1]
                A[5] > A[2] Hence A[5] can be part of sub-sequence that ends at A[2]
                        also currently dp is [1,2,1,1,2,"2",1,1] where dp[5] = 2
                        so if the sub-sequence is [1,6] then length becomes 2 since the length is already 2 we can ignore.
                A[5] > A[3] Hence A[5] can be part of sub-sequence that ends at A[3]
                        also currently dp is [1,2,1,1,2,"2",1,1] where A[5] = 2
                        so if the sub-sequence is [-4,6] then length becomes 2 since the length is already 2 we can ignore.
                A[5] > A[4] Hence A[5] can be part of sub-sequence that ends at A[4]
                        also currently dp is [1,2,1,1,2,"2",1,1] where A[5] = 2
                        Since dp[4] = 2 so if A[5] becomes part of the sub-sequence then the length will increase by 1
                        and will become 3. Hence dp[5] = dp[4] + 1 =3. Now current dp[1,2,1,1,2,3,1,1]

    dp[0,6] = 2
    dp[0,7] = 4


    In dp[i] array store the length of longest increasing sub-sequence that ends at A[i].

"""

def longest_increasing_subsequence(seq):
    if not seq:
        return 0
    dp = [1 for _ in xrange(len(seq))]
    i = 0
    j = 1
    for i in xrange(1, len(seq)):
        for j in xrange(0, i):
            if seq[i] > seq[j]:
                dp[i] = max(dp[j]+1, dp[i])
    return max(dp)

if __name__=="__main__":
    d = [2, 10, 1, -4, 5, 6, 2, 18]
    d = [18,2,3,-1,0,5,15,6,7]
    #d = [1, 2]
    print longest_increasing_subsequence(seq=d)