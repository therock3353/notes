"""
560. Subarray Sum Equals K

    2, 1, -4, 3, 5, -2, 2, 1, -3, 4

    need to find number of subarrays whose sum is 5.

    [1, -4, 3, 5] is one such subarray.

    Brute Force method is find all the subarrays and check if any of their sum is 5

    2, 1, -4, 3, 5, -2, 2, 1, -3, 4
    <----------------------------->
    2, 1, -4, 3, 5, -2, 2, 1, -3, 4
       <-------------------------->
    2, 1, -4, 3, 5, -2, 2, 1, -3, 4
           <---------------------->
    2, 1, -4, 3, 5, -2, 2, 1, -3, 4
              <------------------->

    Explanation regarding alternative approach that will not work in this case:
    ===========================================================================
        Since the numbers can contain -ve numbers, we cannot use sliding window or any such approach.
        if sum is > 5 then increment the start of window(will not work). Since there are -ve numbers, if the subsequent
        number is -ve, the subarray can still be ==5
        1, 2, 1, 4, -3, 2, 4
        i        j
        when we consider this subarray [1, 2, 1, 4] the sum is 8 > 5 but we cannot say that since 8 > 5,
        let's start from i+1 or 2 and check if there are any valid subarrays starting at 2. There
        can still be valid subarrays starting from 1. This happens because -ve numbers are allowed.

    Now we do not want to use brute force method and calculate all subarrays O(n^2)
    This can be solved using maths logic:
    <-x->  <----k---->
    2,     1, -4, 3, 5, -2, 2, 1, -3, 4
    <-------y-------->

    For each iteration add one element to the current Sum.
    if currSum or y is such that y-k = x already exists
    then you found a subarray with sum k

    At each iteration calculate currSum and store in map.

    2, 1, -4, 3, 5, -2, 2, 1, -3, 4
    i                                   FreqMap: 2: 1       (found a subarray with sum 2, once)
    currSum = 2

    2, 1, -4, 3, 5, -2, 2, 1, -3, 4
       i                                FreqMap: 2: 1       (found a subarray with sum 2, once)
    currSum = 3                                  3: 1       (found a subarray with sum 3, once)

    2, 1, -4, 3, 5, -2, 2, 1, -3, 4
          i                             FreqMap: 2: 1       (found a subarray with sum 2, once)
    currSum = -1                                 3: 1       (found a subarray with sum 3, once)
                                                 -1:1       (found a subarray with sum -1, once)

    2, 1, -4, 3, 5, -2, 2, 1, -3, 4
              i                         FreqMap: 2: 2       (found a subarray with sum 2, twice)
    currSum = 2                                  3: 1
                                                 -1:1
    2, 1, -4, 3, 5, -2, 2, 1, -3, 4
                 i                      FreqMap: 2: 2       (found a subarray with sum 2, twice)
    currSum = 7                                  3: 1
                                                 -1:1
                                                 7: 1
             currSum is 7, and we know that there are 2 subarrays whose sum is 2. This means there are
             2 subarrays whose sum is 5.  [5], [1, -4, 3, 5]

"""

class Solution(object):
    def subarraySum(self, nums, k):
        freqMap = {}
        currSum = None
        numOfSubarrays = 0
        for i in range(len(nums)):
            if currSum is None:
                currSum = nums[i]
            else:
                currSum += nums[i]
            if currSum-k in freqMap:
                numOfSubarrays += freqMap.get(currSum-k, 0)
            if currSum in freqMap:
                freqMap[currSum] += 1
            else:
                freqMap[currSum] = 1
        return numOfSubarrays