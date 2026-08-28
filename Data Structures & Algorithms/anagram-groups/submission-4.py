class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        for st in strs:
            sorted_st = ''.join(sorted(st))
            mp[sorted_st].append(st)
        return list(mp.values())
        

