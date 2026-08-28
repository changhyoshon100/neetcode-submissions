class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        L = 0
        visit = set()
        cnt = 1
        for R in range(len(s)):
            
            while s[R] in visit:
                visit.remove(s[L])
                L += 1
            visit.add(s[R])
            cnt = max(len(list(visit)), cnt) 
        return cnt

