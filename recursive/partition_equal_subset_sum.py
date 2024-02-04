'''
    https://leetcode.com/problems/partition-equal-subset-sum/description/
    416. Partition Equal Subset Sum
        Example: nums = [1, 2, 3, 4]
        At each level we have 2 choices, either add the current number to first sum or add the
        current number at second sum

                            [1, 0]                          [0, 1]
                [3, 0]                      [1, 2]
     [6, 0]             [3, 3]          [4,2]   [1, 5]
[10, 0]  [6,4]       [7,3]   [3,7]

Time Complexity: O(2^N)

'''


class Solution(object):
    def partition_recursively(self, A, first_half_sum, second_half_sum):
        if not A:
            if first_half_sum == second_half_sum:
                return True
            else:
                return False
        result = self.partition_recursively(A[1:], first_half_sum+A[0], second_half_sum)
        if result is True:
            return True
        result = self.partition_recursively(A[1:], first_half_sum, second_half_sum+A[0])
        if result is True:
            return True
        return False

    def canPartition(self, nums):
        return self.partition_recursively(nums, 0, 0)


if __name__=="__main__":
    nums = [1,2,3,4]
    print Solution().canPartition(nums)