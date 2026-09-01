class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mp = defaultdict(int)
        for i in range(len(t)):
            mp[t[i]] += 1
        mp2 = defaultdict(int)
        L = 0
        have = 0
        need = len(mp)
        res = [-1,-1]
        resLen = float('inf')
        # print(mp)
        for R in range(len(s)):
            mp2[s[R]] += 1
            if s[R] in mp and mp2[s[R]] == mp[s[R]]:
                have += 1
                # print(mp)
                while have == need:
                    
                    if resLen >= (R - L + 1):
                        
                        res = [L, R]
                        resLen = min(resLen, (R - L + 1))
                    mp2[s[L]] -= 1
                    # print(mp2,s[L], s[L] in mp, mp)
                    if s[L] in mp and mp2[s[L]] < mp[s[L]]:
                        
                        have -= 1
                    L += 1
        L,R = res
        return s[L:R + 1]
                    



