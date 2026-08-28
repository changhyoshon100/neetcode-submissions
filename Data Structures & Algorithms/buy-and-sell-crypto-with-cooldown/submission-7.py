class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            if buying:
                # buying
                buy = dfs(i+1, not buying) - prices[i]
                skip_buy = dfs(i+1, buying)
                dp[(i, buying)] = max(buy, skip_buy)
            else:
                # cooldown
                sell = dfs(i+2, not buying) + prices[i]
                skip_sell = dfs(i+1, buying)
                dp[(i, buying)] = max(sell, skip_sell)
            
            return dp[(i, buying)]

        return dfs(0,True)