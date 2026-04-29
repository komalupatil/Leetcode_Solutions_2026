# https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_map = {}
        for i, num in enumerate(nums):
            complement = target-num
            if complement in sum_map:
                return [sum_map[complement], i]
            sum_map[num] = i
        return []
