class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        mp = defaultdict(int)
        res = 0
        for R, ch in enumerate(s):
            mp[ch] += 1
            while (R - L + 1) - max(mp.values()) > k:
                mp[s[L]] -= 1
                L += 1
            res = max(res, (R - L + 1))
        return res

            
            