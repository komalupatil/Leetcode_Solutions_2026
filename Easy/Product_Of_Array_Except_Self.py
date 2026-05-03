# https://leetcode.com/problems/product-of-array-except-self/description/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]*len(nums)

        for i in range(1, len(nums)):
            left[i] = left[i-1]*nums[i-1]
        
        right = 1
        for j in range(len(nums)-2, -1, -1):
            right = right * nums[j+1]
            left[j] = left[j]*right
        return left

# Solution 2
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]*len(nums)
        right = [1]*len(nums)
        result = [1]*len(nums)
        for i in range(1, len(nums)):
            left[i] = left[i-1]*nums[i-1]
        for j in range(len(nums)-2, -1, -1):
            right[j] = right[j+1]*nums[j+1]
        for k in range(len(nums)):
            result[k] = left[k]*right[k]
        return result

