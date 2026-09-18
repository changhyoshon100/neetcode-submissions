class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        store = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in store:
                store.remove(s[l])
                l += 1
            res = max(len(store), res)
            store.add(s[r])
        # print(store)
        return res + 1