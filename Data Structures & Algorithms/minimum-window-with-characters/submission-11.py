class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mpt = defaultdict(int)
        for i in range(len(t)):
            mpt[t[i]] += 1
        mps = defaultdict(int)
        l = 0
        have = 0
        need = len(mpt)
        res = [-1, -1]
        resLen = float('inf')
        for r in range(len(s)):
            mps[s[r]] += 1
            if s[r] in mpt and mps[s[r]] == mpt[s[r]]:
                have += 1
                while have == need:
                    if resLen >= (r - l + 1):
                        res = [l,r]
                        resLen = min(resLen, (r - l + 1))
                    mps[s[l]] -= 1
                    if s[l] in mpt and mps[s[l]] < mpt[s[l]]:
                        have -= 1
                    l += 1

        l,r = res
        return s[l:r + 1]

                
            
        
