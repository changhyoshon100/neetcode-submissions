class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visit = set()
        cnt = 0
        L = 0
        for R in range(len(s)):
            while s[R] in visit:
                
                visit.remove(s[L])
                L += 1
            visit.add(s[R])
            cnt = max(cnt, len(list(visit)))
            
        return len(list(visit)) if cnt == 0 else cnt
            