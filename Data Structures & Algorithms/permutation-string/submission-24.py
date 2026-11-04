class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mp1 = defaultdict(int)
        for ch in s1:
            mp1[ch] += 1
        mp2 = defaultdict(int)
        L,R = 0,0
        for R in range(len(s2)):
            mp2[s2[R]] += 1
            if R - L + 1 == len(s1):
                if mp1 == mp2:
                    return True
                mp2[s2[L]] -= 1
                if mp2[s2[L]] == 0: del mp2[s2[L]]
                L += 1
        return False
