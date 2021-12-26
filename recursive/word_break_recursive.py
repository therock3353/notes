'''
139. Word Break
Given a string s and a dictionary of strings wordDict, return true if s can be segmented
into a space-separated sequence of one or more dictionary words.

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
'''
from copy import deepcopy

class Solution(object):
    def dfs(self, candidate, remaining, result, results, wordDict):
        if not remaining:
            results.append(deepcopy(result))
            return result

        for i in range(len(remaining)):
            candidate += remaining[i]
            if candidate not in wordDict:
                continue
            result += [candidate]
            self.dfs(candidate="", remaining=remaining[i + 1:], result=result, results=results, wordDict=wordDict)
            result.pop()

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not s:
            return False
        results = []
        self.dfs(candidate="", remaining=s, result=[], results=results, wordDict=wordDict)
        print("Result Combinations are :")
        print(result) # [cat, sand, dog], [cats, and, dog]
        if results:
            return True
        else:
            return False


if __name__=="__main__":
    wordDict = set()
    wordDict.add("cat")
    wordDict.add("cats")
    wordDict.add("sand")
    wordDict.add("san")
    wordDict.add("an")
    wordDict.add("and")
    wordDict.add("dog")
    wordDict.add("at")
    wordDict.add("do")
    word = "catsanddog"
    print(Solution().wordBreak(s=word, wordDict=wordDict))