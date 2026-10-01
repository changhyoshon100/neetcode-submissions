class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in memo:
                return memo[(i,buying)]

            # buying
            if buying:
                # buying, keep
                a = dfs(i + 1, not buying) - prices[i]
                b = dfs(i + 1, buying)
                memo[(i, buying)] = max(a,b)
            # selling
            else:
                # selling, keep
                a = dfs(i + 2, not buying) + prices[i]
                b = dfs(i + 1, buying)
                memo[(i, buying)] = max(a,b)
            return memo[(i, buying)]
            
        return dfs(0, True)