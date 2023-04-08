"""
https://leetcode.com/problems/subsets/
    input is [1,2,3,4]
                    1                       2               3           4
                    |                       |               |
        2           3       4           3       4           4
        |           |                   |
     3     4        4                   4
    |
    4

    O(n) = 2^(N-1) ~= 2^n
        https://stackoverflow.com/a/31237534
"""


class Solution(object):
    def dfs(self, selected, remaining, result):
        result.append(selected)

        for i in range(len(remaining)):
            self.dfs(selected=selected + [remaining[i]],
                     remaining=remaining[i + 1:],
                     result=result)

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []

        result = []
        self.dfs(selected=[], remaining=nums, result=result)

        return result