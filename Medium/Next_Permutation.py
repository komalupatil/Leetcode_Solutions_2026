# https://leetcode.com/problems/next-permutation/description/

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        n = len(nums)
        pivot = -1
        for i in range(n-1, 0, -1):
            if nums[i-1] < nums[i]:
                pivot = i - 1
                break
        if pivot == -1:
            self.reverse(nums, 0, n-1)
            return 
        for i in range(n-1, -1, -1):
            if nums[i] > nums[pivot]:
                nums[i], nums[pivot] = nums[pivot], nums[i]
                break
        self.reverse(nums, pivot+1, n-1)

    

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
