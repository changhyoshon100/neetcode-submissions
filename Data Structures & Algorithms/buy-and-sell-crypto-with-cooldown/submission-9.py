class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i,buying) in memo:
                return memo[(i, buying)]
            
            if buying:
                buy = dfs(i+1, not buying) - prices[i]
                skip = dfs(i+1, buying)
                memo[(i, buying)] = max(buy, skip)
            else:
                sell = dfs(i+2, not buying) + prices[i]
                skip = dfs(i+1, buying)
                memo[(i, buying)] = max(sell, skip)
            return memo[(i, buying)]
        
        return dfs(0, True)