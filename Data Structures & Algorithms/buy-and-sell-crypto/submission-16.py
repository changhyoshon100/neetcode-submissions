class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell = float('-inf')
        buy = float('inf')
        profit = 0
        for i in range(len(prices) - 1):
            buy = min(buy, prices[i])
            sell = prices[i+1]
            profit = max(profit, sell - buy)
        return profit