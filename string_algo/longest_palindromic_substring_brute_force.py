"""
    Find the longest palindrom.
    If the string is "thisaacbcaawjkjaaj" then the longest palindrom is aacbcaa.

    The brute force approach is that we go through character at each index and find the longest
    palindrom centered around this character.

    In the above example : thisaacbcaawjkjaaj
    start with index = 0 , s[0] = t, the longest palindrom whose center is index 0 or char 't' is 1.
    index = 1 , s[1] = h, the longest palindrom whose center is index 1 or char 'h' is 1
    index = 2 , s[2] = i, the longest palindrom whose center is index 2 or char 'i' is 1
    ...
    index = 7 , s[7] = b, the longest palindrom whose center is index 7 or char 'b' is aacbcaa

    To calculate the palindrom from center index s = [a,a,c,b,c,a,a]
             left    i  right
    | a | a |  c   | b | c   | a | a |    s[left] == s[right] so increment the len of palindrom by 2

        left       i      right
    | a | a  | c | b | c |  a  | a |    s[left] == s[right] so increment the len of palindrom by 2

    left          i          right
    | a | a  | c | b | c | a | a |    s[left] == s[right] so increment the len of palindrom by 2



    To calculate the palindrom from center index s = [a,c,c,a]

    left  i  right
    | a | c |  c  | a |    if s[i] == s[i+1] then increment right by 1 and increment the len of palindrom by 1

    left  i      right
    | a | c | c | a |    if s[left] == s[right] increment the len of palindrom by 2

    so length of palindrom in this case is 4.
    In a,c,c,a when index is 2 i.e the 2nd c, it will give the answer as 1 which is ok because we already calculated the
    longest palindrom as 4 when index is 1 i.e 1st c.

"""


#Get longest palindrom centered around index
def get_palindrom(s, index):
    longest_palindrom = s[index]
    len_longest_palindrom = 1
    #check for even pattern
    left = index-1
    right = index+1
    if index+1 < len(s):
        if s[index] == s[index+1]:
            len_longest_palindrom += 1
            longest_palindrom = s[index: index+2]
            right = right + 1
    while left >=0 and right < len(s):
        if s[left] == s[right]:
            len_longest_palindrom +=2
            longest_palindrom = s[left:right+1]
            left -=1
            right +=1
        else:
            break
    return len_longest_palindrom, longest_palindrom

def longest_palindromic_substr(s):
    longest_palindrom = None
    len_of_longest_palindrom = 0
    for i in range(len(s)):
        len_of_palindrom, palindrom = get_palindrom(s, i)
        if len_of_palindrom > len_of_longest_palindrom:
            len_of_longest_palindrom = len_of_palindrom
            longest_palindrom = palindrom

    return len_of_longest_palindrom, longest_palindrom


if __name__ =="__main__":
    s = "thisaacbcaawjkjaaj"
    print longest_palindromic_substr(s)
    # s = "abcba"
    # print get_palindrom(s, 0)
    # print get_palindrom(s, 1)
    # print get_palindrom(s, 2)
    # print get_palindrom(s, 3)