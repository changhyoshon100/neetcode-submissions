class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dp = [float('inf')] * n
        dp[src] = 0
        for i in range(k+1):
            cp = dp.copy()
            for s,d,p in flights:
                if dp[s] == float('inf'):
                    continue
                if dp[s] + p < cp[d]:
                    cp[d] = dp[s] + p
            dp = cp
        return dp[dst] if dp[dst] != float('inf') else -1