"""
77. Combinations https://leetcode.com/problems/combinations/

    for i in range(1, 5):
        subsets(result+[i])

                    1                 2            3           4
             ---------------      ----------    -------     -----      ...
             |   |   |   |        |   |   |      |   |        |
             2   3   4   5        3   4   5      4   5        5
        3  4  5  |   5   (x)   4    5 |   (x)    5   (x)     (x)
               ----                   5
               4   5

    When k=2, we only go one level below and the recursion is cut at that level.

    O(n) == ??

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


class Solution(object):
    def recurse(self, remaining, k, result, results):
        if k == 0:
            results.append(result)
            return

        for i in range(len(remaining)):
            self.recurse(remaining=remaining[i+1:],
                         k=k-1,
                         result=result+[remaining[i]],
                         results=results)
    def combine(self, n, k):
        remaining = [i for i in range(1, n+1)]
        results = []
        self.recurse(remaining=remaining,
                     k=k, result=[], results=results)
        return results

print Solution().combine(5, 3)