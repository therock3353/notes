
"""


"""



def house_robber(welth_data):
    if not welth_data:
        return 0
    if len(welth_data) == 1:
        return welth_data[0]
    dp = [0 for i in xrange(len(welth_data))]

    for i in xrange(len(welth_data)):
        rob = welth_data[i] + (dp[i-2] if i>=2 else 0)
        dont_rob = dp[i-1] if i>=1 else 0
        dp[i] = max(rob, dont_rob)

    print dp
    return dp[-1]

if __name__=="__main__":

    d = [10,4,2,10,5,1,3]
    #d = [0, 0, 0]
    print house_robber(d)