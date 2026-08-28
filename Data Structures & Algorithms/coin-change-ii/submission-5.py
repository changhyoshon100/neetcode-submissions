class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def dfs(i, target):
            
            if i == len(coins) or target > amount:
                return 0
            if target == amount:
                return 1
            if (i,target) in memo:
                return memo[(i,target)]
            memo[(i,target)] = dfs(i, target + coins[i]) + dfs(i+1, target)

            return memo[(i,target)]

        return dfs(0,0)