# https://leetcode.com/problems/reverse-bits/description

class Solution:
    def reverseBits(self, n: int) -> int:
        reversed_n = 0
        for _ in range(32):
            reversed_n = reversed_n << 1 #shift to left
            bit = n&1
            reversed_n = reversed_n  | bit
            n = n >> 1 #shift to right
        return reversed_n
