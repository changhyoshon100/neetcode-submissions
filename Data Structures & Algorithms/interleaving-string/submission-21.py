class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        memo = {}
        
        def dfs(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            k = i + j
            if k == len(s3):
                return True
            
            if i < len(s1) and s1[i] == s3[k] and dfs(i+1, j):
                memo[(i,j)] = True
                return True
            
            if j < len(s2) and s2[j] == s3[k] and dfs(i, j+1):
                memo[(i,j)] = True
                return True

            memo[(i,j)] = False
            return False
        return dfs(0,0)
        