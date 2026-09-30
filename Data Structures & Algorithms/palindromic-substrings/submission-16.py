class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            l,r = i,i
            while 0 <= l < len(s) and 0 <= r < len(s) and s[l] == s[r]:
                ans += 1
                l -= 1
                r += 1
            
            l,r = i,i+1
            while 0 <= l < len(s) and 0 <= r < len(s) and s[l] == s[r]:
                ans += 1
                l -= 1
                r += 1
        return ans
