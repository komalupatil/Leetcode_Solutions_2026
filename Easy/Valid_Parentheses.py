# https://leetcode.com/problems/valid-parentheses/description/

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        if len(s) == 1:
            return False
        opening_brackets = "({["
        bracket_dict = {")": "(", "]":"[", "}": "{"}
        stack = []
        for bracket in s:
            if bracket in opening_brackets:
                stack.append(bracket)
            else:
                if not stack or stack.pop() != bracket_dict[bracket]:
                    return False
        if stack:
            return False
        return True

# Solution 2

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        closing_brackets = []

        for bracket in s:
            if bracket == "(":
                closing_brackets.append(")")
            elif bracket == "[":
                closing_brackets.append("]")
            elif bracket == "{":
                closing_brackets.append("}")
            else:
                if not closing_brackets or closing_brackets.pop() != bracket:
                    return False
        if closing_brackets:
            return False
        return True
