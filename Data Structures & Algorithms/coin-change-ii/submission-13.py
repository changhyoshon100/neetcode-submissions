class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def dfs(i, total):
            if total > amount:
                return 0
            if total == amount:
                return 1
            if i == len(coins):
                return 0
            if (i,total) in memo:
                return memo[(i,total)]
            
            # use
            a = dfs(i, total + coins[i])
            # skip
            b = dfs(i+1, total) 
            memo[(i,total)] = a + b
            return memo[(i,total)]
        return dfs(0, 0)