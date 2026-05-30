# https://leetcode.com/problems/minimum-absolute-difference-between-two-values/description/

class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        idx1 = -1
        idx2 = -1
        res = float('inf')

        for i in range(len(nums)):
            if nums[i] == 1:
                idx1 = i
                if idx2 != -1:
                    res = min(abs(idx2-idx1), res)
            elif nums[i] == 2:
                idx2 = i
                if idx1 != -1:
                    res = min(abs(idx1-idx2), res)
        return -1 if res == float('inf') else res
