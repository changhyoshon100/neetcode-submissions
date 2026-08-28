class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        N = len(coins)
        dp = {}
        def dfs(i, curr):
            if i == N or curr < 0:
                return 0
            if curr == 0:
                return 1
            if (i, curr) in dp:
                return dp[(i, curr)]
            # skip i
            best = dfs(i+1, curr)
            # repeat and include i with if statement
            if curr - coins[i] >= 0:
                best += dfs(i, curr - coins[i])
            dp[(i, curr)] = best
            return best
        return dfs(0, amount)