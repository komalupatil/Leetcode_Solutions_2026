# https://leetcode.com/problems/trapping-rain-water/description/

# Bruteforce

class Solution:
    def trap(self, height: List[int]) -> int:
        totalWater = 0
        for i in range(len(height)):
            leftmax = 0
            for j in range(0, i+1):
                leftmax = max(leftmax, height[j])
            
            rightmax = 0
            for k in range(i, len(height)):
                rightmax = max(rightmax, height[k])
            
            totalWater += (min(leftmax, rightmax) - height[i])
        
        return totalWater
        
# Better than Bruteforce

class Solution:
    def trap(self, height: List[int]) -> int:
        totalWater = 0
        n = len(height)
        leftmax = [0]*n
        leftmax[0] = height[0]
        for j in range(1, n):
            leftmax[j] = max(leftmax[j-1], height[j])
        
        rightmax = [0]*n
        rightmax[n-1] = height[n-1]
        for k in range(n-2, -1, -1):
            rightmax[k] = max(rightmax[k+1], height[k])
        
        

        for i in range(len(height)):
            totalWater += (min(leftmax[i], rightmax[i]) - height[i])
        
        return totalWater
