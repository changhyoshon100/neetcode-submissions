class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        visit = []
        for i in s:
            visit.append(i)
        
        for i in t:
            if not i in visit:
                return False
            
            visit.remove(i)
            
        return True if len(visit) == 0 else False
