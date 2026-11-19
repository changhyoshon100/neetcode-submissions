class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            
            if (i, buying) in memo:
                return memo[(i, buying)]

            # buying
            if buying:
                take = dfs(i+1, not buying) - prices[i]
                skip = dfs(i+1, buying)
                memo[(i, buying)] = max(take, skip)
            # selling
            else:
                take = dfs(i+2, not buying) + prices[i]
                skip = dfs(i+1, buying)
                memo[(i, buying)] = max(take, skip)
            return memo[(i, buying)]

        return dfs(0, True)