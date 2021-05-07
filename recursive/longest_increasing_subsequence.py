


def longest_increasing_subsequence(selected, remaining, len_longest_seq, max_len_longest_seq):
    if not remaining:
        max_len_longest_seq = max(max_len_longest_seq, len_longest_seq)
        return max_len_longest_seq

    for i in range(len(remaining)):
        elem = remaining[i]
        if not selected or elem > selected[-1]:
            max_len_longest_seq = longest_increasing_subsequence(selected=selected+[remaining[i]],
                                           remaining=remaining[i+1:],
                                           len_longest_seq=len_longest_seq+1, max_len_longest_seq=max_len_longest_seq)
            #len_longest_seq-=1
        # max_len_longest_seq = longest_increasing_subsequence(selected=selected,
        #                                remaining=remaining[i+1:],
        #                                len_longest_seq=len_longest_seq, max_len_longest_seq=max_len_longest_seq)

    return max_len_longest_seq




if __name__=="__main__":
    d = [18,2,3,-1,0,5,15,6,7]

    d = [2,10,1,-4, 5, 6, 2, 18]
    print longest_increasing_subsequence(selected=[], remaining=d, len_longest_seq=0, max_len_longest_seq=0)