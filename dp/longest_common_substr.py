"""
    Longest Common Substring using Dynamic Programming

    | a  | b  | c  | d  | e  | f  | g  | h  |
  m | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  |
  c | 0  | 0  | 1  | 0  | 0  | 0  | 0  | 0  |
  d | 0  | 0  | 0  | 2  | 0  | 0  | 0  | 0  |
  e | 0  | 0  | 0  | 0  | 3  | 0  | 0  | 0  |
  a | 1  | 0  | 0  | 0  | 0  | 0  | 0  | 0  |
  b | 0  | 2  | 0  | 0  | 0  | 0  | 0  | 0  |

 - Check if "m" matches with a  - no -> 0
 - Check if "m" matches with b  - no -> 0
 - Check if "m" matches with c  - no -> 0
 - Check if "m" matches with d  - no -> 0
 - Check if "m" matches with e  - no -> 0
 ....

 - Check if "c" matches with a  - no -> 0
 - Check if "c" matches with b  - no -> 0
 - Check if "c" matches with c  - Yes ->
When c from "abc" and "mc" match, we add 1 (because both are c) to the result
of if "b" from "ab" and "m" match. (they don't match so it is 0+1 = 1 in "abc" match "mc" column
 - Check if "c" matches with d  - no -> 0
 - Check if "c" matches with e  - no -> 0
...


 - Check if "d" matches with a  - no -> 0
 - Check if "d" matches with b  - no -> 0
 - Check if "d" matches with c  - no -> 0
 - Check if "d" matches with d  - Yes ->
When d from "abcd" and "mcd" match, we add 1 to the result of
    if c from "abc" and c from "mc" match.
 - Check if "d" matches with e  - no -> 0
 - Check if "d" matches with f  - no -> 0
...

The length of longest common substring between S1 and S2 is the max(dp[[]])

Operational Complexity is O(m*n)
"""

def longest_common_substr(s1, s2):
    lcs = ""
    dp =[]

    for row_id in range(len(s2)):
        row = [0 for _ in range(len(s1))]
        dp.append(row)
    for row in dp:
        print row
    print "==============================="
    for i in range(len(s2)):
        for j in range(len(s1)):
            if s2[i] == s1[j]:
                if i == 0 or j ==0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = 0
    for row in dp:
        print row
    print "==============================="

    len_lcs = 0
    max_i = max_j = 0
    for i in range(len(s2)):
        for j in range(len(s1)):
            if dp[i][j] > len_lcs:
                len_lcs = dp[i][j]
                max_i = i
                max_j = j
    print "=== max_i {}, === max_j {}, === dp[i][j] {} ===".format(max_i, max_j, len_lcs)

    while max_i >= 0 and max_j >= 0 and dp[max_i][max_j] > 0:
        lcs += s1[max_j]
        max_i -= 1
        max_j -= 1

    return lcs[::-1]

if __name__=="__main__":

    s1 = "abcdefgh"
    s2 = "mcdeab"

    s1 = "abc"
    s2 = "amajkabcioei"
    print longest_common_substr(s1, s2)