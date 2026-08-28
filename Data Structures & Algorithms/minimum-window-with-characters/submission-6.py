class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = [-1,-1]
        resLen = float('infinity')
        countT = defaultdict(int)
        window = defaultdict(int)

        for i in range(len(t)):
            countT[t[i]] += 1
        need = len(countT)
        have = 0
        L = 0
        for R in range(len(s)):
            ch = s[R]
            window[ch] += 1
            if window and window[ch] == countT[ch]:
                have += 1
            while have == need:
                if resLen > R - L + 1:
                    resLen = (R - L + 1)
                    res = [L,R]
                window[s[L]] -= 1
                if s[L] in countT and window[s[L]] < countT[s[L]]:
                    have -= 1
                L += 1
        L,R = res
        return s[L:R+1] if resLen != float('infinity') else ""

        
