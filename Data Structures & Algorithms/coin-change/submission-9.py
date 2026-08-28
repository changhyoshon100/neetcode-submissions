class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        ans = 0
        memo = {}

        def dfs(i, total):
            if total > amount or i == len(coins):
                return float('inf')
            if total == amount:
                return 0
            if (i,total) in memo:
                return memo[(i,total)]
            

            use = 1 + dfs(i, total + coins[i])
            skip = dfs(i+1, total)
            memo[(i,total)] = min(use, skip)

            return memo[(i,total)]
        ans = dfs(0,0) 
        return ans if ans != float('inf') else -1