class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        mp = defaultdict(int)
        cnt = 0
        for R in range(len(s)):
            mp[s[R]] += 1
            while (R - L + 1) - max(mp.values()) > k:
                mp[s[L]] -= 1
                L += 1
            
            cnt = max(cnt, R - L + 1)
        return cnt
            
