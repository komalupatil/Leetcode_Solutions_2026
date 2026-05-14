# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0]
        max_profit = 0

        for price in prices:
            max_profit = max(max_profit, price-minimum)
            minimum = min(minimum, price)
        return max_profit
