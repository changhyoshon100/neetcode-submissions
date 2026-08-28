class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N = len(profit)
        memo = {}

        def dfs(i, curr):
            if i == N:
                return 0
            if curr <= 0:
                return 0
            if (i, curr) in memo:
                return memo[(i, curr)]
            
            # skip i
            best = dfs(i+1, curr)

            # repeat and include i with if statement 
            if curr - weight[i] >= 0:
                best = max(best, profit[i] + dfs(i, curr - weight[i]))
            memo[(i, curr)] = best
            return best
        return dfs(0, capacity)