# https://leetcode.com/problems/minimum-number-of-food-buckets-to-feed-the-hamsters/description/

class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        hamsters_l = list(hamsters)
        for i in range(len(hamsters_l)):
            if hamsters_l[i] == 'H':
                if i > 0 and hamsters_l[i-1] == 'B':
                    continue
                if i < len(hamsters_l)-1 and hamsters_l[i+1] == ".":
                    hamsters_l[i+1] = 'B'
                elif i > 0 and hamsters_l[i-1] == '.':
                    hamsters_l[i-1] = 'B'
                else:
                    return -1
        hamsters_s = "".join(hamsters_l)
        return hamsters_s.count('B')

# Solution 2

class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        return -1 if 'HHH' in hamsters or hamsters[:2] == 'HH' or hamsters[-2:] == 'HH' or hamsters == 'H' else hamsters.count('H') - hamsters.count('H.H')
     
