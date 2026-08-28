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
            a,b = i, i
            cnt = max(cnt, pal(a,b,cnt))

            # even
            a,b = i, i+1
            cnt = max(cnt, pal(a,b,cnt))
        return cnt
            