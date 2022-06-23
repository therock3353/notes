"""
    EPI 12.6 - Smallest Subarray covering all values
    Leetcode 76. Minimum Window Substring

    You are given a text and few words. Need to find smallest substring (represented by start and end index)
     in text which cover all the words.

    words = ["this", "is", "sparta"]
    text = ["thin", "is", "a", "part", "of", "this", "would",
            "is", "a", "is", "sparta", "this", "bay", "this", "wo", "is", "sparta", "test", "best"]
    Ans: ["is", "sparta", "this"]

    s = "ADOBECODEBANC"
    t = "ABC"
    Ans: "BANC"

    keep two maps (remaining_words) and already_found_word.
    remaining_words = {word: word_freq}
    already_found_word = {word: first_index}

    i = 0
    j = 0
    i is start ptr, j is end ptr.
    - start from 0 and iterate through text using j untill you find all the words in words_list.
    - once you know this substr, calculate substr len, check if smallest.
    - start the above search for words from sorted(already_found_word) #by index to get the index of first word found + 1
    - i = new_index, reset j = i
        
"""
from collections import Counter
def smallest_subarray(text, words):
    if not text or not words:
        return
    i = 0
    j = 0
    already_found_words = {}
    remaining_words = Counter(words)
    result = []
    while i < len(text) and j < len(text):
        if text[j] in words:
            if text[j] in already_found_words:
                already_found_words[text[j]][1] = j
                remaining_words[text[j]] -= 1
                if remaining_words[text[j]] <= 0:
                    remaining_words.pop(text[j], None)
            else:
                already_found_words[text[j]] = [j, -1]
                remaining_words[text[j]] -= 1
                if remaining_words[text[j]] <= 0:
                    remaining_words.pop(text[j], None)
            if not remaining_words:
                sorted_lst = sorted(already_found_words.items(), key=lambda e: e[1][0])
                min = sorted_lst[0][1][0]
                max = sorted_lst[-1][1][1]
                if max == -1:
                    max = sorted_lst[-1][1][0]
                if not result:
                    result = [min, max]
                else:
                    prev_len = result[1] - result[0]
                    if (max - min) < prev_len:
                        result = [min, max]
                remaining_words = Counter(words)
                already_found_words = {}
                i = min + 1
                j = min + 1
            else:
                j += 1
        else:
            j += 1
    if not result:
        return ""
    return text[result[0]: result[1]+1]

if __name__=="__main__":
    words = ["this", "is", "sparta"]
    text = ["thin", "is", "a", "part", "of", "this", "would",
            "is", "a", "is", "sparta", "this", "bay", "this", "wo", "is", "sparta", "test", "best"]
    s = "ADOBECODEBANC"
    t = "ABC"
    print smallest_subarray(s, t)
