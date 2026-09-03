class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minSoFar = prices[0]
        profit = 0
        for p in prices:
            profit = max(profit, p - minSoFar)
            minSoFar = min(minSoFar, p)
        return profit