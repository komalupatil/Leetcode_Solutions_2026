# https://leetcode.com/problems/container-with-most-water/description/

# similar approach to trapping rain water

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n-1
        ans = 0
        while left < right:
            if height[left] < height[right]:
                ht = height[left]
                wd = abs(left-right)
                left += 1
            else:
                ht = height[right]
                wd = abs(left-right)
                right -= 1
            ans = max(ans, ht*wd)
        return ans
