class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mp = defaultdict(int)
        for i in range(len(s1)):
            mp[s1[i]] += 1
        
        need = len(mp)

        for i in range(len(s2)):
            mp2 = defaultdict(int)
            cur = 0
            for j in range(i, len(s2)):
                if s2[j] not in mp:
                    break
                mp2[s2[j]] += 1
                
                if mp2[s2[j]] > mp[s2[j]]:
                    break
                
                if mp2[s2[j]] == mp[s2[j]]:
                    cur += 1
                
                if need == cur:
                    return True
        return False

            