class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1: return s
        resLen = 0
        res = ""
        for i in range(len(s)):
            # odd
            l,r = i, i
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resLen = r - l + 1
                    res = s[l:r+1]
                r += 1
                l -= 1
                
            # even
            l,r = i, i+1
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resLen = r - l + 1
                    res = s[l:r+1]
                r += 1
                l -= 1
        return res