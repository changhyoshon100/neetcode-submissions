class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3): return False
        if len(s1) == 0 and len(s2) == 0: return not len(s3)
        if len(s1) == 0: return s2 == s3
        if len(s2) == 0: return s1 == s3

        memo = {}

        def dfs(i,j, mixed):
            if i + j == len(s3) - 2 and mixed == s3[:len(mixed)]:
                return True
            if i == len(s1) or j == len(s2): 
                return False
            if mixed != s3[:len(mixed)]:
                return False

            if (i,j) in memo:
                return memo[(i,j)]
            
            a = dfs(i+1,j, mixed + s1[i])
            b = dfs(i,j+1, mixed + s2[j])
            
            memo[(i,j)] = a or b
            return memo[(i,j)]
            
        return dfs(0,0, "")