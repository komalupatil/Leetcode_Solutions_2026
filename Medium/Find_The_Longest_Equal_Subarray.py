# https://leetcode.com/problems/find-the-longest-equal-subarray/description/
class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        positions = defaultdict(list)
        for i, num in enumerate(nums):
            positions[num].append(i)
        answer = 1

        for value, pos in positions.items():
            left = 0
            for right in range(len(pos)):
                window_size = pos[right] - pos[left] + 1
                count = right - left + 1
                deletions = window_size - count

                while deletions > k:
                    left += 1
                    window_size = pos[right] - pos[left] + 1
                    count = right - left + 1
                    deletions = window_size - count
                answer = max(answer, count)

        return answer
