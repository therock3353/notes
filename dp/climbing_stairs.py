"""
    Climb Stairs using DP:

    If the steps you can do are 2 or 3 steps at a time.
    dp[0] = 0
    dp[1] = 0
    dp[2] = 1
    dp[3] = 1
    dp[4] = dp[4-2] + dp[4-3] # you can go to 4-2 = 2nd stair and then take 2 step or you can go to 4-3 = 1st stair and then take 3 step.
    dp[5] = dp[5-2] + dp[5-3]
    dp[6] = dp[6-2] + dp[6-3]
    dp[7] = dp[7-2] + dp[7-3]
    ...
    ...


"""


def num_of_ways_claimbing_stairs(final_stairs, step1, step2):
    if final_stairs == 0:
        return 0
    if final_stairs == 1:
        return 1
    if not step1 and not step2:
        return 0
    no_of_ways_dp = []
    min_step = min(step1, step2)
    for _ in range(final_stairs+1):
        no_of_ways_dp.append(0)

    for i in range(min_step, final_stairs+1, 1):
        on_ith_step = 0
        first_ans = 0
        second_ans = 0
        if i == step1 or i == step2:
            on_ith_step = 1
        if (i - step1) >= 0:
            first_ans = no_of_ways_dp[i-step1]
        else:
            first_ans = 0
        if (i - step2) >= 0:
            second_ans = no_of_ways_dp[i-step2]
        else:
            second_ans = 0

        no_of_ways_dp[i] = first_ans + second_ans  + on_ith_step


    no_of_ways = no_of_ways_dp[-1]
    return no_of_ways


if __name__=="__main__":
    steps = [2,3]
    n = 12
    print num_of_ways_claimbing_stairs(n, steps[0], steps[1])