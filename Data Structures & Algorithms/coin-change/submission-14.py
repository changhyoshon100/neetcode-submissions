class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(i,target):
            if i == len(coins) or target > amount:
                return float('inf')
            
            if target == amount:
                return 0
            
            if (i, target) in memo:
                return memo[(i, target)]
            
            # use
            use = 1 + dfs(i, target + coins[i])

            # skip
            skip = dfs(i+1, target)
            memo[(i,target)] = min(use, skip)

            return memo[(i,target)]
            
        ans = dfs(0,0)
        return ans if ans != float('inf') else -1