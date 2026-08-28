class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        durations = [1, 7, 30]
        N = len(days)
        dp = {}
        def dfs(i):
            if i == N:
                return 0
            if i in dp:
                return dp[i]
            res = float("inf")
            for cost, duration in zip(costs, durations):
                j = i
                while j < len(days) and days[j] < days[i] + duration:
                    j += 1
                res = min(res, cost + dfs(j))
            dp[i] = res
            return res
        return dfs(0)