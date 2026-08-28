class Solution:
    def longestCommonSubsequence(self, t1: str, t2: str) -> int:
        memo = {}
        def dfs(i1,i2):
            if i1 == len(t1) or i2 == len(t2):
                return 0
            if (i1, i2) in memo:
                return memo[(i1,i2)]
            if t1[i1] == t2[i2]:
                
                memo[(i1, i2)] = 1 + dfs(i1+1, i2+1)
                return memo[(i1, i2)]
            else:
                memo[(i1, i2)] = max(dfs(i1+1, i2), dfs(i1, i2+1))
                return memo[(i1, i2)]
            return memo[(len(t1)-1, len(t2)-1)]
        return dfs(0,0)