# https://leetcode.com/problems/number-of-1-bits/description

class Solution:
    def hammingWeight(self, n: int) -> int:
        counts = 0
        while n != 0:
            counts += n&1
            n = n >> 1
        return counts
