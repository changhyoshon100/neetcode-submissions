class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: 
            print('34')
            return 0
        L = 0
        res = 0
        mp = defaultdict(int)
        for R in range(len(s)):
            if s[R] in mp:
                if L < mp[s[R]]:
                    L = mp[s[R]]
            
            mp[s[R]] = R + 1
            res = max(res, R - L)
        return res + 1
            