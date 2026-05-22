# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/description/

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        day = events[0][0]
        i = 0
        count = 0
        n = len(events)
        minHeap = []
        while (i < n or len(minHeap) != 0):
            while i < n and events[i][0] == day:
                heapq.heappush(minHeap, events[i][1])
                i += 1
            if minHeap:
                heapq.heappop(minHeap)
                count += 1
            day += 1
            while len(minHeap) != 0 and minHeap[0] < day:
                heapq.heappop(minHeap)

        return count

