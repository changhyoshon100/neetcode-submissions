class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        sell = float('-inf')
        maxProfit = 0
        for i in range(len(prices) - 1):
            buy = min(buy, prices[i])
            sell = prices[i+1]
            
            maxProfit = max(maxProfit, sell - buy)
        return maxProfit

