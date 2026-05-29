# https://leetcode.com/problems/interval-list-intersections/description/

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        a = 0
        b = 0

        intervals = []
        while a < len(firstList) and b  < len(secondList):
            interval_start, interval_end = max(firstList[a][0], secondList[b][0]), min(firstList[a][1], secondList[b][1])

            if interval_start <= interval_end:
                intervals.append([interval_start, interval_end])
            
            if firstList[a][1] < secondList[b][1]:
                a += 1
            else:
                b += 1
        return intervals
         
