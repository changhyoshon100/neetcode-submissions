class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = defaultdict(int)
        window = defaultdict(int)
        for k in t:
            countT[k] += 1
        resLen = float('inf')
        L = 0
        have = 0
        need = len(countT)
        res = [-1,-1]
        for R in range(len(s)):
            window[s[R]] += 1

            if window and window[s[R]] == countT[s[R]]:
                have += 1
            
            while have == need:
                if resLen > (R - L + 1):
                    resLen = (R - L + 1)
                    res = [L, R]
                window[s[L]] -= 1
                if window and window[s[L]] < countT[s[L]]:
                    have -= 1
                L += 1
        L, R = res
        return s[L:R + 1] if resLen != float('inf') else ""

            