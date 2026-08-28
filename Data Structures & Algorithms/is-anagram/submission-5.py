class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mp = defaultdict(int)
        for n in s:
            mp[n] += 1
        
        for n in t:
            if n in mp:
                mp[n] -= 1
            else:
                return False
            if mp[n] < 0:
                return False
            
       
        
        return sum(mp.values()) == 0