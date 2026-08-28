class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}
        def dfs(i,j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            
            if (i,j) in memo:
                return memo[(i,j)]
            
            
            # same
            if s[i] == t[j]:
                a = dfs(i+1,j+1)
                b = dfs(i+1,j)
                memo[(i,j)] = a + b
            # different
            else:
                memo[(i,j)] = dfs(i+1,j)
            return memo[(i,j)]
        
        return dfs(0,0)