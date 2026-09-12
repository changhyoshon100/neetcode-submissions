class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = float('inf')
        memo = {}
        def dfs(i, total):
            if total == amount:
                return 0
            if total > amount or i == len(coins):
                return float('inf')
            if (i,total) in memo:
                return memo[(i,total)]
            
            a = dfs(i, total + coins[i]) + 1
            b = dfs(i+1, total)
            memo[(i,total)] = min(a,b)
            return memo[(i,total)]
        ans = dfs(0,0) 
        return ans if ans != float('inf') else -1
        