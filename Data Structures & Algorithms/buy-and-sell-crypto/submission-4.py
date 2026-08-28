class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        small, large = prices[0], prices[0]
        res = 0
        for i in range(1,len(prices)):
            large = max(prices[i], prices[i-1])
            small = min(prices[i-1], small)
            if small < large:
                res = max(res, large - small)
        return res