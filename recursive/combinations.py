"""

    for i in range(1, 5):
        subsets(result+[i])

        1                   2                   3                   4
 -----------------    ---------------    ----------------     --------------      ...
 |   |   |   |   |    |  |  |   |   |    |   |  |   |   |     |  |  |   |   |
 1   2   3   4   5    1  2  3   4   5    1   2  3   4   5     1  2  3   4   5

    When k=2, we only go one level below and the recursion is cut at that level.

"""

def subsets(n, k, x, result, results):
    if len(result) == k:
        results.append(result)
        return

    for i in range(x, n+1):
        subsets(n, k, i+1, result+[i], results)

    return results

if __name__=="__main__":
    n = 5
    k = 3
    # [
    #   [1, 2], [1, 3], [1, 4], [1, 5],
    #   [2, 3], [2, 4], [2, 5],
    #   [3, 4], [3, 5],
    #   [4, 5]
    # ]
    print subsets(n, k, 1, [], [])