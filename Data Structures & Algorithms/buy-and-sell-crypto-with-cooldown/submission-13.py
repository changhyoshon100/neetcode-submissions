class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dfs(i, state):
            if i >= len(prices):
                return 0
            if (i,state) in memo:
                return memo[(i,state)]
            # cooldown
            cooldown = dfs(i+1, state)

            # buy
            if state:
                buy = dfs(i+1, not state) - prices[i]
                memo[(i, state)] = max(buy, cooldown)
            else:
                sell = dfs(i+2, not state) + prices[i]
                memo[(i, state)] = max(sell, cooldown)
            return memo[(i,state)]

        return dfs(0,True)