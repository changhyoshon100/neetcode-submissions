class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mp = defaultdict(int)
        mp2 = defaultdict(int)
        res = [-1,-1]
        
        for ch in t:
            mp2[ch] += 1
        
        L = 0
        have = 0
        resLen = float('inf')
        need = len(mp2)
        for R in range(len(s)):
            mp[s[R]] += 1
            if s[R] in mp and mp[s[R]] == mp2[s[R]]:
                have += 1
                while have == need:
                    if (R - L + 1) <= resLen:
                        res = [L,R]
                        resLen = R - L + 1
                    mp[s[L]] -= 1
                    if s[L] in mp2 and mp[s[L]] < mp2[s[L]]:
                        have -= 1
                    L += 1
        a,b = res
        return s[a:b+1]
                    



