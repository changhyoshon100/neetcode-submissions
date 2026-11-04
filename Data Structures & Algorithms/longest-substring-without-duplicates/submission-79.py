class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashSet = set()
        L, R = 0, len(s) - 1
        res = 0
        for R in range(len(s)):
            while s[R] in hashSet:
                hashSet.remove(s[L])
                L += 1
            hashSet.add(s[R])
            res = max(res, R - L + 1)
        return res
            