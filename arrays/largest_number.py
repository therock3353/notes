from functools import cmp_to_key

"""


"""
class Solution(object):
    def largestNumber(self, nums):
        def compare(x, y):
            if x+y > y+x:
                return 1
            elif x == y:
                return 0
            else:
                return -1

        nums = [str(num) for num in nums]
        nums.sort(key=cmp_to_key(compare), reverse=True)
        print nums
        return ''.join(nums).lstrip('0')


if __name__ == "__main__":
    A = [5, 6, 3, 42, 23]  # [6542323] [65]
    print Solution().largestNumber(A)
