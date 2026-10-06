class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = 0
        memo = {}

        def dfs(i,total):
            if total == amount:
                return 0
            if total > amount:
                return float('inf')
            
            if i == len(coins):
                return float('inf')
            
            if (i,total) in memo:
                return memo[(i,total)]

            memo[(i,total)] = min(dfs(i, total + coins[i]) + 1, dfs(i+1, total))
            return memo[(i,total)]
        
        ans = dfs(0,0)
        return ans if ans != float('inf') else -1