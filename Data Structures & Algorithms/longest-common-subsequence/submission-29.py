class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        ROWS, COLS = len(text1), len(text2)
        dp = [[0] * (COLS + 1) for _ in range(ROWS + 1)]
        res = []

        for r in range(1, ROWS + 1):
            for c in range(1, COLS + 1):
                if text1[r-1] == text2[c-1]:
                    dp[r][c] = dp[r-1][c-1] + 1
                else:
                    dp[r][c] = max(dp[r][c-1], dp[r-1][c])
        
        i,j = ROWS, COLS
        
        while i > 0 and j > 0:
            if text1[i - 1] == text2[j - 1]:
                res.append(text1[i-1])
                i -= 1
                j -= 1
            elif dp[i][j-1] < dp[i-1][j]:
                i -= 1
            else:
                j -= 1
        
        return len(res)




