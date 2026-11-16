class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(i, res):
            if res == amount:
                return 0
            if i == len(coins):
                return float('inf')
            if res > amount:
                return float('inf')
            if (i, res) in memo:
                return memo[(i, res)]

            take = dfs(i, res + coins[i]) + 1
            skip = dfs(i+1, res)

            memo[(i,res)] = min(take, skip)
            return memo[(i,res)]
        ans = float('inf')
        ans = dfs(0, 0)
        return ans if ans != float('inf') else -1