class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mp_s1 = defaultdict(int)
        for c in s1:
            mp_s1[c] += 1
        
        mp_s2 = defaultdict(int)

        L = 0
        st_s1 = sorted(s1)
        for R in range(len(s2)):
            if s2[R] in s1:
                L = R
                temp = L + len(s1)
                if sorted(s2[L:temp]) == st_s1:
                    return True
        return False
                
            
