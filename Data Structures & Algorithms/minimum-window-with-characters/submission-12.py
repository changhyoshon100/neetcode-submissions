class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mpt = defaultdict(int)
        for i in range(len(t)):
            mpt[t[i]] += 1
        
        mps = defaultdict(int)

        have = 0
        need = len(mpt)
        resLen = float('inf')
        res = [-1,-1]
        L = 0
        for R in range(len(s)):
            mps[s[R]] += 1
            if s[R] in mps and mps[s[R]] == mpt[s[R]]:
                have += 1
                while have == need:
                    if resLen >= (R - L + 1):
                        resLen = min(resLen, R - L + 1)
                        res = [L,R]
                    mps[s[L]] -= 1
                    if s[L] in mpt and mps[s[L]] < mpt[s[L]]:
                        have -= 1
                    L += 1

        L,R = res
        return s[L:R + 1]



