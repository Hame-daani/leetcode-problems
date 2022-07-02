# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        O(N)
        """
        buy = prices[0]
        max_profit = 0
        for sell in prices:
            max_profit = max(sell - buy, max_profit)
            buy = min(buy, sell)
        return max_profit


print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
