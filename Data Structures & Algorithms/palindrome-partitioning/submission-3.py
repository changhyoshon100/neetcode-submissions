class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        bucket = []
        def pali(i,j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        def dfs(i):
            if i == len(s):
                bucket.append(res.copy())
                return 
            
            for j in range(i, len(s)):
                if pali(i,j):
                    res.append(s[i:j+1])
                    dfs(j+1)
                    res.pop()
            return bucket
                
        return dfs(0)
        
        
