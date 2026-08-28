import sys
sys.setrecursionlimit(1000000)

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(i, res):
            if res == amount:
                return 0
            if res > amount or i >= len(coins):
                return float('inf')
            if (i, res) in memo:
                return memo[(i, res)]

            use = 1 + dfs(i, res + coins[i])
            skip = dfs(i + 1, res)

            memo[(i, res)] = min(use, skip)
            return memo[(i, res)]

        ans = dfs(0, 0)
        return -1 if ans == float('inf') else ans