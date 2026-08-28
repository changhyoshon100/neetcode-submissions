class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1 = defaultdict(int)
        dic2 = defaultdict(int)
        if len(s) != len(t): return False
        for i in range(min(len(s), len(t))):
            dic1[s[i]] += 1
            dic2[t[i]] += 1
        
        return dic1 == dic2