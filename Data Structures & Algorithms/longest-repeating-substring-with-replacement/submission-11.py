class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = defaultdict(int)
        L = 0
        res = 0
        for i,v in enumerate(s):
            mp[v] += 1
            
            while (i - L + 1) - max(mp.values()) > k:
                mp[s[L]] -= 1
                L += 1
            
            res = max(res, i - L + 1)
            
            if mp[v] == mp.values():
                res -= 1

        return res
                
