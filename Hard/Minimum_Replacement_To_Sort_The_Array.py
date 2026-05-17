# https://leetcode.com/problems/minimum-replacements-to-sort-the-array/description/
# https://www.youtube.com/watch?v=2QEcQe95_ro
class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        res = 0
        maxMinVal = nums[-1]
        n = len(nums)
        for i in range(n-2, -1, -1):
            if nums[i] <= maxMinVal:
                maxMinVal = nums[i]
            else:
                parts = (nums[i] + maxMinVal -1)//maxMinVal
                res += parts-1
                maxMinVal = nums[i] // parts
        return res
