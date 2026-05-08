# https://leetcode.com/problems/roman-to-integer/description/

class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        if len(s) == 1:
            return symbols[s[0]]
        if len(s) == 0:
            return 0 
        num = 0
        i = 0
        while i < len(s):
            curr_char = symbols[s[i]]
            next_char = 0
            if i+1 < len(s):
                next_char = symbols[s[i+1]]
            if curr_char < next_char:
                num = num + (next_char - curr_char)
                i += 2
            else:
                num = num + curr_char
                i += 1
        return num
