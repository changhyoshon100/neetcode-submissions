class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mp1 = defaultdict(int)
        for i in range(len(s1)):
            mp1[s1[i]] += 1
        mp2 = defaultdict(int)
        l = 0
        for r in range(len(s2)):
            mp2[s2[r]] += 1
            while r - l + 1 > len(s1):
                mp2[s2[l]] -= 1
                if mp2[s2[l]] == 0:
                    del mp2[s2[l]]
                l += 1
                
            if r - l + 1 == len(s1):
                if mp1 == mp2:
                    return True
            
            
        return False


            

        