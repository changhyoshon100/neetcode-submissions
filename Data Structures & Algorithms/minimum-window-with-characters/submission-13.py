class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mp = defaultdict(int)
        mp2 = defaultdict(int)

        for i in range(len(t)):
            mp2[t[i]] += 1
        L = 0
        have = 0
        need = len(mp2)
        resLen = float('inf')
        res = [-1,-1]

        for R in range(len(s)):
            mp[s[R]] += 1
            if s[R] in mp and mp[s[R]] == mp2[s[R]]:
                have += 1
                while have == need:
                    if resLen >= R - L + 1:
                        resLen = R - L + 1
                        res = [L,R]
                    mp[s[L]] -= 1
                    if s[L] in mp2 and mp[s[L]] < mp2[s[L]]:
                        have -= 1
                    L += 1
        L,R = res
        return s[L: R + 1]

        