# https://leetcode.com/problems/search-insert-position/description/

# binary search appraoch 

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        mid = n-1//2
        left = 0
        right = n-1
        while left <= right:
            mid = left + (right-left)//2
            if target > nums[mid]:
                left = mid + 1 
            elif target <= nums[mid]:
                right = mid - 1
            else:
                return mid
        return left
