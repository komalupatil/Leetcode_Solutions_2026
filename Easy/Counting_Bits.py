# https://leetcode.com/problems/counting-bits/description

# similar to number of 1 bits

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(0, n+1):
            count = self.getOneBitCount(i)
            ans.append(count)
        return ans
        
    def getOneBitCount(self, num):
        count = 0
        while num != 0:
            count += num&1
            num = num >> 1
        return count

# DP, number of bits fro even are same as num/2 and for odd are num/2 bits + 1
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]
        for i in range(1, n+1):
            count = self.getOneBitCount(i)
            ans.append(count)
        return ans
        
    def getOneBitCount(self, num):
        count = 0
        while num != 0:
            count += num&1
            num = num >> 1
        return count

        
