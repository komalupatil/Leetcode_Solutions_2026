# https://leetcode.com/problems/can-place-flowers/description/

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        if n == 1 and len(flowerbed) == 1:
            if flowerbed[0] == 0:
                return True
            else:
                return False
        for i, fl in enumerate(flowerbed):
            if fl == 1:
                continue
            elif 0<i<len(flowerbed)-1:
                if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    n -= 1
                    if n == 0:
                        return True
            else:
                if i == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    n -= 1
                    if n == 0:
                        return True
                elif i == len(flowerbed) -1 and flowerbed[i-1] == 0:
                    flowerbed[i] = 1
                    n -= 1
                    if n == 0:
                        return True
        return False

# Better than prvious solution 

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed)-1):
            if flowerbed[i-1] == flowerbed[i] == flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    return True
        return False


