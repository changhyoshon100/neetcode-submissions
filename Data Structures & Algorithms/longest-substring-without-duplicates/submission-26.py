class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visit = set()
        N = len(s)
        if N == 0:
            return 0
        L = 0
        res = 0
        globRes = 0
        
        for R in range(N):
            while s[R] in visit:
                res = max(R - L, res)
                print(res)
                visit.remove(s[L])
                L += 1
            visit.add(s[R])
            globRes = max(res, R - L + 1)
            
        return globRes if globRes != 0 else N


