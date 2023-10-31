class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict = {} # {char:lastAppear}

        leftMost = 0
        currMaxLen = 0
        for i in range(len(s)):
            if s[i] in dict:
                leftMost = max(leftMost, dict[s[i]] + 1)
            currMaxLen = max(currMaxLen, i - leftMost + 1)
            dict[s[i]] = i
        
        return currMaxLen

