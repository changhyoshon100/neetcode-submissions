class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        hash1 = Counter(s1)
        
        l = 0
        r = len(s1)
        hash2 = Counter(s2[l:r])
        
        while r < len(s2):
            if hash1 == hash2: return True
            else:
                hash2[s2[l]] -= 1
                l += 1

                hash2[s2[r]] += 1
                r += 1
        return hash1 == hash2
                