class Solution:
    def longestCommonSubsequence(self, t1: str, t2: str) -> int:
        N = len(t1)
        M = len(t2)
        
        dp = [0] * (M+1)
        
        for i in range(N):
            curRow = [0] * (M+1)    
            for j in range(M):
                if t1[i] == t2[j]:
                    curRow[j+1] = 1 + dp[j]
                else:
                    curRow[j+1] = max(curRow[j], dp[j+1])
            dp = curRow
        return dp[M]