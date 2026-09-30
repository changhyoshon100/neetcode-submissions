class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def dfs(i, total):
            if i >= len(cost):
                return 0
            if i in memo:
                return memo[i]
            
            memo[i] = min(dfs(i+1, total), dfs(i+2, total)) + cost[i]
            return memo[i]
        
        return min(dfs(0,0), dfs(1,0))