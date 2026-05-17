# https://leetcode.com/problems/maximum-number-of-removable-characters/description/

class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def is_subsequence(k):
            removed = set(removable[:k])
            i = 0
            for j, ch in enumerate(s):
                if j in removed:
                    continue
                if i < len(p) and ch == p[i]:
                    i += 1
                if i == len(p):
                    return True
            return i == len(p)


        lo, hi = 0, len(removable)
        ans = 0
        while lo <= hi:
            mid = (lo + hi)//2
            if is_subsequence(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans
