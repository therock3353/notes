
l = ['i', 'am', 'ace', 'a']
l = ['cats', 'and', 'dog', 'at', 'do', 'a', 'an']
#l = ['bull', 'she', 'it', 'hit'] #bullshit
DICTIONARY = set(l)

def is_word_in_dict(wrd, dictionary, dp, i, j):
    if wrd in dictionary:
        dp[i][j] = 1
        return

    for x in range(len(wrd)-1):
        if dp[i][x] == 1 and dp[x+1][j] == 1:
            dp[i][j] = 1

def word_break_dp(word, dictionary):
    dp = []
    for i in range(len(word)):
        dp.append([0 for j in range(len(word))])

    for k in range(0, len(word)):
        for i in range(0, len(word)-k):
            j = i+k
            wrd = word[i: j+1]
            is_word_in_dict(wrd, dictionary, dp, i, j)

    return dp[0][-1]

if __name__=="__main__":

    word = "iamace"
    word = 'catsanddog'
    #word = 'bullshit'
    print word_break_dp(word, DICTIONARY)