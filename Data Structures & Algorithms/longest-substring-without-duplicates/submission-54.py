class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L,R = 0,0
        res = set()
        ans = 0
        for R in range(len(s)):
            if s[R] not in res:
                res.add(s[R])
            else:
                while s[R] in res:
                    res.remove(s[L])
                    L += 1
                res.add(s[R])
            ans = max(ans, len(list(res)))
        return ans
            


        