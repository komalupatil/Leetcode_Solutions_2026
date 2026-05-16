# https://leetcode.com/problems/longest-valid-parentheses/description/

# Bruteforce (time limit exceeds) 

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        def isValid(sub: str) -> bool:
          stack = []
          for ch in sub:
              if ch == '(':
                  stack.append(ch)
              else:  # ch == ')'
                  if not stack:
                      return False
                  stack.pop()
          return len(stack) == 0

        n = len(s)
        max_len = 0
        # Try every substring of even length
        for i in range(n):
            for j in range(i + 2, n + 1, 2):  # step by 2 → only even lengths
                if isValid(s[i:j]):
                    max_len = max(max_len, j - i)
        return max_len

# Using stack (o(n) and o(n))

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]  # sentinel base
        max_len = 0
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            else:  # ')'
                stack.pop()
                if not stack:
                    stack.append(i)  # new base
                else:
                    max_len = max(max_len, i - stack[-1])
        return max_len

# constant space 

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left = right = 0
        maxLen = 0
        for ch in s:
            if ch == "(":
                left += 1
            else: 
                right +=1 
            if left == right:
                maxLen = max(maxLen, 2*right)
            elif right > left:
                left = right = 0
        left = right = 0
        for ch in reversed(s):
            if ch == "(":
                left += 1
            else:
                right += 1
            if left == right:
                maxLen = max(maxLen, 2*left)
            elif left > right:
                left = right = 0
        return maxLen
