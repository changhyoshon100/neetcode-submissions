class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = {}
        res = False
        def dfs(i,j):
            nonlocal res
            if i == len(s1) and j == len(s2) and i+j == len(s3):
                return True
            if (i,j) in memo:
                return memo[(i,j)]
            
            if i < len(s1) and i+j < len(s3) and s1[i] == s3[i+j]:
                res = res or dfs(i+1,j)
            if j < len(s2) and i+j < len(s3) and s2[j] == s3[i+j]:
                res = res or dfs(i,j+1)
            memo[(i,j)] = res
            return memo[(i,j)]
            

        return dfs(0,0)