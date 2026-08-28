class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        l,mp = 0,{}
        ans = 0
        for i in range(len(s)):
            if s[i] in mp:
                l = max(mp[s[i]]+1, l)
            mp[s[i]] = i
            ans = max(ans, i - l + 1)
        return ans
