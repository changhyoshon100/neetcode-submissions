class Solution:
    def countSubstrings(self, s: str) -> int:
        cnt = 0
        def pal(a,b,cnt):
            while a >= 0 and b <= len(s) - 1 and s[a] == s[b]:
                cnt += 1
                a -= 1
                b += 1
            return cnt
        
        for i in range(len(s)):
            # odd
            l,r = i,i
            cnt = max(cnt, pal(l,r,cnt))
            
            # even
            l,r = i,i+1
            cnt = max(cnt, pal(l,r,cnt))
        return cnt