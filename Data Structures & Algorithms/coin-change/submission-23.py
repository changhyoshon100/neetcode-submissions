class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(i,val):
            if val == amount:
                return 0
            if val > amount:
                return float('inf')
            if i == len(coins):
                return float('inf')
            if (i,val) in memo:
                return memo[(i,val)]
        
            a = dfs(i, val + coins[i]) + 1
            b = dfs(i+1, val)
            memo[(i,val)] = min(a,b)
            return memo[(i,val)]

        ans = dfs(0,0)
        return ans if ans != float('inf') else -1