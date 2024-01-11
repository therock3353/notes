

def is_valid_combination(s):
    if 1 <= int(s) <= 26:
        return 1
    else:
        return 0

# def decode_ways(s):
#     num_of_ways = 0
#     if not s:
#         return num_of_ways
#     if len(s) == 1:
#         if 1 <= int(s) <= 26:
#             num_of_ways+=1
#         return num_of_ways
#
#     for i in range(1, len(s)):
#         num_of_ways = num_of_ways + is_valid_combination(s[i]) + is_valid_combination(s[i-1:i+1])
#
#     return num_of_ways


class Solution(object):

    def dfs(self, s, num_ways):
        if not s:
            num_ways += 1
            return num_ways

        if not s[0].startswith("0") and is_valid_combination(s[0]):
            num_ways = self.dfs(s[1:], num_ways)

        if len(s) >= 2 and not s[0].startswith("0") and is_valid_combination(s[0:2]):
            num_ways = self.dfs(s[2:], num_ways)

        return num_ways

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        num_ways = self.dfs(s, 0)
        return num_ways


if __name__=="__main__":

    s = "1010"
    print(Solution().numDecodings(s))