class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        for s in strs:
            sorted_arr = sorted(s)
            sorted_s = ''.join(sorted_arr)
            
            mp[sorted_s].append(s)
        return list(mp.values())

