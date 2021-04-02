

def longest_substr_with_atmost_k_uniq_char(s, k):
    if not s or len(s)==1:
        return s
    if k == 0:
        return None
    if k == 1:
        return s[1]
    len_longest_substr = 0
    uniq_chars = {}
    left = 0
    right = 0
    while right < len(s):
        if len(uniq_chars) < k:
            if s[right] not in uniq_chars:
                uniq_chars[s[right]] = 1
            else:
                uniq_chars[s[right]] += 1
        elif len(uniq_chars) == k:
            if s[right] in uniq_chars:
                uniq_chars[s[right]] += 1
            else:
                if len_longest_substr < (right-left):
                    len_longest_substr = right-left
                while len(uniq_chars) >= k and left < right:
                    if uniq_chars[s[left]] > 1:
                        uniq_chars[s[left]] -= 1
                    else:
                        uniq_chars.pop(s[left])
                    left +=1
                if s[right] not in uniq_chars:
                    uniq_chars[s[right]] = 1
                else:
                    uniq_chars[s[right]] += 1
        right += 1

    if len_longest_substr < (right - left):
        len_longest_substr = right - left

    return len_longest_substr

if __name__=="__main__":

    #s = "ababccc"
    s = "aaabbb"
    #s = "aabbcccc"
    s = "abcddedee"
    k = 2
    print longest_substr_with_atmost_k_uniq_char(s, k)