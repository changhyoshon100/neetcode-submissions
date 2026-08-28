class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(i, target):
            if i == len(coins) or target > amount:
                return float('inf')
            if target == amount:
                return 0
            if (i, target) in memo:
                return memo[(i,target)]

            
            memo[(i,target)] = min(
                # include
                1 + dfs(i, target + coins[i]),
                # not include
                dfs(i+1, target)
            )

            return memo[(i,target)]

        ans = dfs(0,0) 
        return ans if ans != float('inf') else -1