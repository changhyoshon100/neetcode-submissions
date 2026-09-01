class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        hash1 = defaultdict(int)
        for s in s1:
            hash1[s] += 1
        
        hash2 = defaultdict(int)
        for i in range(len(s1)):
            hash2[s2[i]] += 1
        if hash1 == hash2:
            return True
        L = 0

        for R in range(len(s1), len(s2)):
            # print(hash2)
            
            hash2[s2[R]] += 1
            hash2[s2[L]] -= 1
            if hash2[s2[L]] <= 0: del hash2[s2[L]]
            if hash1 == hash2: return True
            L += 1
        return False
            