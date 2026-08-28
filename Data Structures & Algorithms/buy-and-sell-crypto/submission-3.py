class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mi = prices[0]
        ma = prices[0]
        ans = 0
        for i in range(1, len(prices)):
            mi = min(mi, prices[i-1])
            ma = prices[i]
            ans = max(ans, ma - mi)
        return ans