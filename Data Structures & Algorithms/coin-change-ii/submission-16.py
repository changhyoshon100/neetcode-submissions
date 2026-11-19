class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def dfs(i, total):
            if i == len(coins):
                return 0
            if total > amount:
                return 0
            if total == amount:
                return 1
            if (i, total) in memo:
                return memo[(i, total)]
            
            take = dfs(i, total + coins[i])
            skip = dfs(i+1, total)
            memo[(i,total)] = take + skip
            return memo[(i, total)]
        
        return dfs(0, 0)