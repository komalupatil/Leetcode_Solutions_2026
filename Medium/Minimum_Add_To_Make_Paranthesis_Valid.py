# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description/

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        ans = 0
        open = 0
        for ch in s:
            if ch == "(":
                open += 1
            else:
                if open == 0:
                    ans += 1
                else:
                    open -= 1
        return ans + open 
