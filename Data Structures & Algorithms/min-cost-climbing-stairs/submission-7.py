class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def dfs(i,res):
            if i >= len(cost):
                return res
            if (i,res) in memo:
                return memo[(i,res)]
            memo[(i, res)] = min(dfs(i+1, res + cost[i]), dfs(i+2, res + cost[i]))
            
            return memo[(i,res)]
        return min(dfs(0,0), dfs(1,0))