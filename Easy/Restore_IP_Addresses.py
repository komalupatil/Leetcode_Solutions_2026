# https://leetcode.com/problems/restore-ip-addresses/description/
# Solution 1 - Bruteforce
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        n = len(s)
        if n<4 or n > 12:
            return result
        
        def is_valid(segment):
            if len(segment) == 0 or len(segment) > 3:
                return False
            if len(segment) > 1 and segment[0] == "0":
                return False
            return int(segment) <= 255
    
        for i in range(1, 4):
            for j in range(i+1, i+4):
                for k in range(j+1, j+4):
                    if k >= n:
                        continue
                    seg1 = s[0:i]
                    seg2 = s[i:j]
                    seg3 = s[j:k]
                    seg4 = s[k:n]

                    if (is_valid(seg1) and is_valid(seg2) and is_valid(seg3) and is_valid(seg4)):
                        result.append(f"{seg1}.{seg2}.{seg3}.{seg4}")
        return result

# Solution 2 - optimal backtracking
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        n = len(s)
        if n<4 or n > 12:
            return result
        def backtrack(i, dots, currIP):
            if dots == 4 and i == len(s):
                result.append(currIP[:-1])
                return 
            for j in range(i, min(i+3, len(s))):
                if int(s[i:j+1]) <= 255 and (i==j or s[i]!= "0"):
                    backtrack(j+1, dots+1, currIP + s[i:j+1] + ".") 
        backtrack(0, 0, "")
        return result
