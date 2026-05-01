# https://leetcode.com/problems/longest-common-prefix/description/
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        minLength = len(strs[0])
        for k in range(1, len(strs)):
            minLength = min(minLength, len(strs[k]))
        j = 0
        lcp = ""
        while j < minLength:
            char = strs[0][j]
            for i in range(1, len(strs)):
                if char != strs[i][j]:
                    return lcp
            lcp = lcp + char
            j += 1
        return lcp
