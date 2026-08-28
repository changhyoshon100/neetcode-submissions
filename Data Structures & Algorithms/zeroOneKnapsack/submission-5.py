class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        memo = {}
        n = len(profit)
        def dfs(i, cap):
            if i == n:
                return 0
            if cap <= 0:
                return 0
            if (i, cap) in memo:
                return memo[(i, cap)]
            # skip i
            best = dfs(i+1, cap)

            # take i 
            if cap - weight[i] >= 0:
                best = max(best, profit[i] + dfs(i+1, cap - weight[i]))

            memo[(i, cap)] = best
            return best
        

        return dfs(0, capacity)