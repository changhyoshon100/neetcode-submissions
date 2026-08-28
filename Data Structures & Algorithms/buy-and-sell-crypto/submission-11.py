class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        low = prices[0]
        for i in range(1, len(prices)):
            if low > prices[i]:
                low = prices[i]
            else:
                profit = max(profit, prices[i] - low)
        return profit
            