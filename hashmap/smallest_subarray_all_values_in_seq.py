"""
    EPI 12.8 Smallest Subarray sequentially covering all values

    text = ["thin", "is", "a", "part", "of", "this", "would",
            "is", "a", "is", "sparta", "this", "bay", "this", "wo", "is", "sparta", "test", "best"]
    words = ["this", "is", "sparta"]

    start = 5, end = 10 ["this", "would", "is", "a", "is", "sparta"] => len = 5
    start = 13, end = 16 ["this", "wo", "is", "sparta"] => len = 3
    smallest substr = 3

    while text_idx < len(text):
        #if word matches text's current word:
            if this is 1st word:
                initialize start ptr of substr
            match next word now #wrd_ptr += 1
        #if all words in words are matched:
            calculate curr substr len
            if curr_len < longest:
                longest = curr_len
            start_ptr = -1
            wrd_ptr = 0

        text_idx += 1

    The special case to consider:
        text = ["this", "this", "this", "is", "sparta"]
                0         1       2       3      4
            here our start index needs to be 2 and not 0.

    Time Complexity => O(n)

"""

def smallest_subarry(text, words):
    if not text or not words:
        return 0
    txt_ptr = 0
    wrd_ptr = 0
    smallest_substr_len = float('inf')
    start_substr_idx = -1
    while txt_ptr < len(text):
        if start_substr_idx != -1 and text[txt_ptr] == words[0]:
            start_substr_idx = txt_ptr
        if words[wrd_ptr] == text[txt_ptr]:
            if wrd_ptr == 0:
                start_substr_idx = txt_ptr
            wrd_ptr += 1
        if wrd_ptr >= len(words):
            curr_substr_len = txt_ptr - start_substr_idx
            if curr_substr_len < smallest_substr_len:
                smallest_substr_len = curr_substr_len
            wrd_ptr = 0
            start_substr_idx = -1
        txt_ptr += 1

    return smallest_substr_len

if __name__=="__main__":
    text = ["thin", "is", "a", "part", "of", "this", "would",
            "is", "a", "is", "sparta", "this", "bay", "this", "wo", "is", "sparta", "test", "best"]
    words = ["this", "is", "sparta"]
    print smallest_subarry(text, words)