# https://leetcode.com/problems/calculate-amount-paid-in-taxes/description/
class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        result = 0
        if len(brackets) == 0:
            return result
        if brackets[0][0] <= income:
            result += (brackets[0][0] * brackets[0][1]/100)
        else:
            result += income * brackets[0][1]/100
        if len(brackets) == 1:
            return result
        for i in range(1, len(brackets)):
            if brackets[i][0] > income:
                result += ((income - min(brackets[i-1][0], income)) * brackets[i][1]/100)
            else:
                result += ((brackets[i][0] - min(brackets[i-1][0], income)) * brackets[i][1]/100)
        return result

        
