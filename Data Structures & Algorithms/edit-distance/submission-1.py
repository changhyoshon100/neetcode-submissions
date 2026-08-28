class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        
        def dfs(i1, i2):
            if i1 == m:
                return n - i2
            if i2 == n:
                return m - i1
            
            if word1[i1] == word2[i2]:
                return dfs(i1+1, i2+1)
            else:
                res = min(dfs(i1+1, i2), dfs(i1, i2+1))
                res = min(res, dfs(i1+1, i2+1))
            return res + 1
        
        return dfs(0,0)