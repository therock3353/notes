'''
leetcode problem 91

    input: 1231
    We check max 2 possibilities in each step:
        - is 1st digit mapping to any letter?
        - is 1st 2 digits mapping to any letter?
    We check 2 possibilities because we are given letters between A-Z which correspond to digits 1-26.

                    1                       12
            2               23          3       31(X)
        3      31(X)    1           1
     1

Since in each step we can have 2 options 1st char (s[0]) or 1st 2 char (s[:2]) & there are N digits
    Time Complexity: O(2^N)
    Space Complexity: O(N)
'''


def is_valid_combination(s):
    if s is not None and len(s) > 0:
        if s.startswith("0"):
            return False
        if 1 <= int(s) <= 26:
            return True
    return False

def decode_ways_dfs(remaining, numOfWays):
    if not remaining:
        numOfWays += 1
        return numOfWays

    if is_valid_combination(remaining[:1]) and len(remaining)>=1:
        numOfWays = decode_ways_dfs(remaining[1:], numOfWays)
    if is_valid_combination(remaining[:2]) and len(remaining)>=2:
        numOfWays = decode_ways_dfs(remaining[2:], numOfWays)
    return numOfWays

def decode_ways(s):
    if not s:
        return 0
    return decode_ways_dfs(remaining=s, numOfWays=0)

if __name__=="__main__":
    s = "1231"
    print(decode_ways(s))