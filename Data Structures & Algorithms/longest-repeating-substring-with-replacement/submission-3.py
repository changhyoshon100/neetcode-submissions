class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = defaultdict(int)
        res = 0
        L = 0
        N = len(s)
        res = 0
        for R in range(N):
            mp[s[R]] += 1
            while (R - L + 1) - max(mp.values()) > k:
                mp[s[L]] -= 1
                L += 1
        
            res = max(res, R - L + 1)
        return res

        