"""
    Robot can go right side or down. It cannot go up or left side.

    | 0 | 1  | 1  |
    | 1 | 2  | 3  |
    | 1 | 3  | 6  |
    | 1 | 4  | 10 |

    One can reach (0,1) in 1 way    (0,0) -> (0,1)  [right]
    One can reach (0,2) in 1 way    (0,0) -> (0,1) -> (0,2) [right, right]
    One can reach (1,0) in 1 way    (0,0) -> (1,0) [down]
    One can reach (2,0) in 1 way    (0,0) -> (1,0) -> (2,0) [down, down]
    One can reach (1,1) in 2 ways   num_of_ways from (0,1) + num_of_ways from (1,0) = 1+1
                                    [down, right] + [right, down] = 2 ways
    One can reach (2,1) in 3 way    num_of_ways from (2,0) + num_of_ways from (1,1) = 1+2 = 3
                                    [down, down, right] + {[down, right, down],[right, down, down]} = 3


    Operational complexity is O(m*n)

"""


def unique_paths(m, n):
    if m <= 0 or n <= 0:
        return 0
    dp = []
    for _ in xrange(m):
        dp.append([0 for _ in xrange(n)])

    for row_id in xrange(len(dp)):
        for col_id in xrange(len(dp[0])):
            if row_id == 0:
                dp[row_id][col_id] = 1
            elif col_id == 0:
                dp[row_id][col_id] = 1
            else:
                dp[row_id][col_id] = dp[row_id-1][col_id] + dp[row_id][col_id-1]

    return dp[-1][-1]

if __name__=="__main__":

    m = 4
    n = 4

    print unique_paths(m, n)