class Solution:
    def longestPalindrome(self, s: str) -> str:
        resLen = 0
        res = ""

        for i in range(len(s)):
            l,r = i,i
            while (0 <= l < len(s) and 0 <= r < len(s)) and s[l] == s[r]: 
                if (r - l + 1) > resLen:
                    resLen = r - l + 1
                    res = s[l: l + resLen]
                l -= 1
                r += 1
                
        for i in range(len(s)):
            l,r = i,i+1
            while (0 <= l < len(s) and 0 <= r < len(s)) and s[l] == s[r]: 
                if (r - l + 1) > resLen:
                    resLen = r - l + 1
                    res = s[l: l + resLen]
                l -= 1
                r += 1
        return res