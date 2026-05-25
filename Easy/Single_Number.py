# https://leetcode.com/problems/single-number/description

# XOR 
# 0 ^ 0 = 0
# 1^ 1 = 0
# 1 ^ 0 = 1
# 0 ^ 1 = 1

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res = n ^ res
        return res
