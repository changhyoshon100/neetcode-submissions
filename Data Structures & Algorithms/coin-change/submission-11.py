class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(total,i):
            if total == amount:
                return 0
            if total > amount or i == len(coins):
                return float('inf')
            if (total,i) in memo:
                return memo[(total, i)]

            use = 1 + dfs(total + coins[i], i) 
            skip = dfs(total, i+1)
            memo[(total,i)] = min(use, skip)
            return memo[(total, i)]
        ans = dfs(0,0)
        return ans if ans != float('inf') else -1