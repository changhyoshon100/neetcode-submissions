class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def dfs(i):
            if i >= len(cost):
                return 0
            if i in memo:
                return memo[i]
            
            a = dfs(i+1) 
            b = dfs(i+2)
            memo[i] = min(a,b) + cost[i]
            return memo[i]
        
        res = float('inf')
        for i in range(2):
            memo = {}
            res = min(dfs(i), res)
        return res