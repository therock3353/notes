# coding=utf-8
"""
    Longest Palindrom in a string using brute force.

    Calculate the longest palindrom centered at each index of the string.
    s = "abmqapopap"

    Longest palindrom centered at index 0 and char 'a' is 'a'
    Longest palindrom centered at index 1 and char 'b' is 'a'
    Longest palindrom centered at index 2 and char 'm' is 'a'
    Longest palindrom centered at index 3 and char 'q' is 'a'
    Longest palindrom centered at index 4 and char 'a' is 'a'
    Longest palindrom centered at index 5 and char 'p' is 'p'
    Longest palindrom centered at index 6 and char 'o' is 'apopa'
    Longest palindrom centered at index 7 and char 'p' is 'p'
    Longest palindrom centered at index 8 and char 'a' is 'pap'

    O(n) = 1 + 2 + 3 + ... + n/2 + ... + 3 + 2 + 1
             n/2
        2 * ( Σ ) i
             i=0
"""

def longest_palindrom_centered_at(s, index):
    palindrom = ""
    start = index
    end = index
    while start-1 >= 0 and s[start-1] == s[index]:
        start -= 1
    while end+1 < len(s) and s[end+1] == s[index]:
        end += 1

    while start >= 0 and end < len(s):
        if s[start] != s[end]:
            break
        else:
            palindrom = s[start: end+1]
        start -= 1
        end += 1

    return palindrom

def longest_palindromic_substr_brute_force(s):
    if not s:
        return s
    if len(s) == 1:
        return len(s)

    longest_palindrom = ""
    for i in range(len(s)):
        palindrom = longest_palindrom_centered_at(s, i)
        if len(palindrom) > len(longest_palindrom):
            longest_palindrom = palindrom

    return longest_palindrom


if __name__=="__main__":

    s = "abmqapopap"
    s = "abbba"
    print longest_palindromic_substr_brute_force(s)