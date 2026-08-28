class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = defaultdict(int)
        window = defaultdict(int)
        res = [-1,-1]
        resLen = float("infinity")

        for i in range(len(t)):
            countT[t[i]] += 1
        have = 0
        need = len(countT)
        L = 0
        for R in range(len(s)):
            ch = s[R]
            window[ch] += 1
            
            if ch in countT and window[ch] == countT[ch]:
                have += 1
            
            while have == need:
                if (R - L + 1) < resLen:
                    res = [L, R]
                    resLen = (R - L + 1)
                window[s[L]] -= 1
                if s[L] in countT and window[s[L]] < countT[s[L]]:
                    have -= 1
                L += 1
        L,R = res
        return s[L:R + 1] if resLen != float("infinity") else "" 
                
                
            
            
            
            