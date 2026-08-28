class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = 10**9
        memo = {}
        def dfs(i,curr):
            if curr == 0:
                return 0
            if i == len(coins) or curr < 0:
                return INF
            if (i, curr) in memo:
                return memo[(i, curr)]
            
            # skip i 
            best = dfs(i+1, curr)
            
            # include i 
            if curr - coins[i] >= 0:
                best = min(best, 1 + dfs(i, curr - coins[i]))
            memo[(i, curr)] = best
            return best
        
        ans = dfs(0,amount)
        return -1 if ans >= INF else ans