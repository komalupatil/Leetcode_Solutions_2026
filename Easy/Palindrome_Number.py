# https://leetcode.com/problems/palindrome-number/
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        num, result = x, 0

        while num:
            result = result*10 + num%10
            num //= 10
        return result == x
