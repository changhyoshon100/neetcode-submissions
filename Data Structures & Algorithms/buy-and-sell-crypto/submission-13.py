class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float('inf')
        sell = float('-inf')
        profit = 0
        for i in range(len(prices)-1):
            buy = min(prices[i], buy)
            sell = prices[i+1]
            
            profit = max(sell - buy, profit)
        
        return profit
            