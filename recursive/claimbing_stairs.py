
"""
                                10
                                 |
                            ------------
                  (2 steps) |           |  (3 steps)
                            8           7
                          -----      -------
                          |    |     |      |
           (2 steps)     6     5     5      4  (3 steps)
                      ------  ----  ----    ----
                      |     | |   | |   |   |   |
                      4     3 3   2 3   2   2   1
                    -----
                    |
                    2
"""

def climb_stairs(n, num_of_ways=0):
    if n == 2 or n == 3:
        num_of_ways+= 1
        return num_of_ways
    if n <2:
        return num_of_ways

    for i in [2, 3]:
        num_of_ways = climb_stairs(n=n-i, num_of_ways=num_of_ways)

    return num_of_ways

if __name__=="__main__":
    #If you have to take 2 or 3 steps at a time, how many number of ways you can climb upto 12th stair.
    x = 10
    print climb_stairs(x)