class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        store = [0, 1]
        k = 1
        while k <= n:
            tmp = store[1]
            store[1] = store[1] + store[0]
            store[0] = tmp
            k += 1
        return store[1]

# def dp(n):
#     if n < 2:
#         return n

#     dp = [0, 1]
#     i = 2
#     while i <= n:
#         tmp = dp[1]
#         dp[1] = dp[0] + dp[1]
#         dp[0] = tmp
#         i += 1
#     return dp[1]