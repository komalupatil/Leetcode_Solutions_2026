# https://leetcode.com/problems/teemo-attacking/description/

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0
        result = 0
        start = timeSeries[0]
        end = timeSeries[0] + duration
        for i in range(1, len(timeSeries)):
            if timeSeries[i] > end:
                result += end-start
                start = timeSeries[i]
            end = timeSeries[i] + duration 
        result += end - start 
        return result

# Solution 2

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0
        total = 0
        
        for i in range(len(timeSeries)-1):
            total += min (timeSeries[i+1]-timeSeries[i], duration)
        return total + duration
