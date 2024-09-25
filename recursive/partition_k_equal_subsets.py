'''
https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
    Partition array into k buckets so that each bucket has same sum.

    At each iteration, the choice is should I put this number into a bucket or not.
    O(N) = k^n
    There are 2 implementations, both inefficient :)
    Approach1 (Iterate over number of buckets):
        In each bucket, put 1 number and recurse.

        for i in range(k):
            currSum = result[i] + nums[0]
            if currSum > target:
                continue
            result[i] += nums[0]
            dfs(nums[1:], result)
            result[i] -= nums[0]

    Approach2 (Iterate over given numbers, one bucket at a time):

        for i in range(len(nums)):
            currSum = result[bucketId] + nums[i]
            if currSum > target:
                continue
            result[bucketId] += nums[i]
            if currSum == target:
                dfs(remaining, bucketId+1)
            else:
                dfs(remaining, bucketId)
            result[i] -= nums[0]


'''

class Solution(object):
    def dfs(self, nums, result, target, k):
        if not nums:
            for s in result:
                if s != target:
                    return False
            return True

        for i in range(k):
            currSum = result[i] + nums[0]
            if currSum > target:
                continue
            result[i] += nums[0]
            res = self.dfs(nums[1:], result, target, k)
            if res is True:
                return res
            result[i] -= nums[0]
        return False

    def canPartitionKSubsets(self, nums, k):
        result = [0 for _ in range(k)]
        total = sum(nums)
        target = total / k
        res = self.dfs(nums, result, target, k)
        return res


class Solution(object):

    def dfs(self, nums, bucketId, result, target, k):
        if bucketId >= k and not nums:
            return True
        if bucketId >= k:
            return False
        if not nums:
            return False
        for i in range(len(nums)):
            currSum = result[bucketId] + nums[i]
            if currSum > target:
                continue
            result[bucketId] += nums[i]
            if currSum == target:
                res = self.dfs(nums[:i]+nums[i+1:], bucketId+1, result, target, k)
                if res is True:
                    return res
            else:
                res = self.dfs(nums[:i]+nums[i+1:], bucketId, result, target, k)
                if res is True:
                    return True
            result[bucketId] -= nums[i]
        return False

    def canPartitionKSubsets(self, nums, k):
        result = [0 for _ in range(k)]
        total = sum(nums)
        target = int(total / k)
        res = self.dfs(nums, 0, result, target, k)
        return res


# print(Solution().canPartitionKSubsets([4,3,2,3,5,2,1], 4))
print(Solution().canPartitionKSubsets([1,2,3,4], 3))