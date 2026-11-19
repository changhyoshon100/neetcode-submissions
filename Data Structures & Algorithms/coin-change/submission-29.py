class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(i, total):
            if total == amount:
                return 0
            if i >= len(coins) or total > amount:
                return float('inf')
            if (i, total) in memo:
                return memo[(i,total)]

            take = dfs(i, total + coins[i]) + 1
            skip = dfs(i+1, total)
            memo[(i,total)] = min(take, skip)
            return memo[(i,total)]
        ans = 0
        ans = dfs(0, 0)
        return ans if ans != float('inf') else -1