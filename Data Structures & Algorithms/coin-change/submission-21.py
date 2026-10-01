class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(i,total):
            if i >= len(coins) or total > amount:
                return float('inf')
            if total == amount:
                return 0
            if (i,total) in memo:
                return memo[(i,total)]
            
            a = dfs(i, total + coins[i]) + 1 
            b = dfs(i+1, total) 
            memo[(i,total)] = min(a,b)
            return memo[(i,total)]
        
        ans = dfs(0,0)
        return ans if ans != float('inf') else -1