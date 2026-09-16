class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dfs(i, state):
            if i >= len(prices):
                return 0
            if (i,state) in memo:
                return memo[(i,state)]
            
            if state:
                buying = dfs(i+1, not state) - prices[i]
                cooldown = dfs(i+1, state)
                memo[(i,state)] = max(buying, cooldown)
            else:
                sell = dfs(i+2, not state) + prices[i]
                cooldown = dfs(i+1, state)
                memo[(i,state)] = max(sell, cooldown)
            return memo[(i,state)]
        
        return dfs(0, True)