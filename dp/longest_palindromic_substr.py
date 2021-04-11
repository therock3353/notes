

def longest_palindrom_dp(s):
    if not s:
        return s
    if len(s) == 1:
        return s
    longest_palindrom = ""
    curr_palindrom = ""
    dp = []
    for i in range(len(s)):
        row = [0 for i in range(len(s))]
        dp.append(row)

    for i in range(len(s)):
        for j in range(i, i+1, 1):
            if i == j:
                dp[i][j] = 1
            elif j < len(s) and s[i] == s[j]:
                dp[i][j] = 1

    for step in range(2, len(s), 1):
        for i in range(len(s)-step):
            j = i + step
            if s[i] == s[j] and dp[i+1][j-1] == 1:
                dp[i][j] = 1
                curr_palindrom = s[i:j+1]
                if len(curr_palindrom) > len(longest_palindrom):
                    longest_palindrom = curr_palindrom

    for i in dp:
        print i
    return longest_palindrom



if __name__=="__main__":

    s = "abmqapopap"
    print longest_palindrom_dp(s)