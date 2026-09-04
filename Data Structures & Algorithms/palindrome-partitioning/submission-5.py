class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        subsets = []
        
        def palindrome(i,j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        def dfs(i):
            if i == len(s):
                res.append(subsets.copy())
                return 
            
            for j in range(i, len(s)):
                if palindrome(i,j):
                    subsets.append(s[i:j+1])
                    dfs(j+1)
                    subsets.pop()
        dfs(0)
        return res
        