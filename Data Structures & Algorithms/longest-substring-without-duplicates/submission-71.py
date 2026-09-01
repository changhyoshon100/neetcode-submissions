class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1: return 1
        if not s: return 0
        L = 0
        store = set()
        res = 0
        for R in range(len(s)):
            while s[R] in store:
                res = max(res, (R - L))
                store.remove(s[L])
                L += 1
                
            store.add(s[R])
            
            res = max(res, (R - L + 1))
            # print(res)
        return res if res != 0 else len(s)

            