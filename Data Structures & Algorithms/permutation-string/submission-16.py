class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mp = defaultdict(int)
        L, R = 0,0
        for i in range(len(s1)):
            mp[s1[i]] += 1
        store = mp.copy()
        # print(store)
        for R in range(len(s2)):
            if s2[R] in mp and R + len(s1) <= len(s2):
                
                part = s2[R: R + len(s1)]
                # print(part)
                for p in part:
                    mp[p] -= 1
                # print(mp)
                
                if min(mp.values()) == 0 and max(mp.values()) == 0: 
                    return True
                mp = store.copy()
                
            
            # print(store)
        return False
