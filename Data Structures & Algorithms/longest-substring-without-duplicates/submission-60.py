class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1: return 1
        check = set()
        L = 0
        res = 0
        for R in range(len(s)):
            while s[R] in check:
                # res = max(res, R - L)
                check.remove(s[L])
                L += 1
            check.add(s[R])
            res = max(res, R - L + 1)
        
        return res if res != 0 else len(check)