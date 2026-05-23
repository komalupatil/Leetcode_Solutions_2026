# https://leetcode.com/problems/median-of-two-sorted-arrays/description/

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B, = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total//2

        if len(A) > len(B):
            A, B = B, A
        
        l, r = 0, len(A)-1
        while True:
            aMid = (l+r)//2
            bMid = half - aMid - 2

            ALeft = A[aMid] if aMid >= 0 else float("-inf")
            ARight = A[aMid+1] if aMid+1 < len(A) else float("+inf")
            BLeft = B[bMid] if bMid >= 0 else float("-inf")
            BRight = B[bMid+1] if bMid+1 < len(B) else float("+inf")

            if ALeft <= BRight and BLeft <= ARight:
                # odd
                if total %2:
                    return min(ARight, BRight)
                else:
                   return (max(ALeft, BLeft) + min(ARight, BRight))/2
            elif ALeft > BRight:
                r = aMid - 1
            else:
                l = aMid + 1
