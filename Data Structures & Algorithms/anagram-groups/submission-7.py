class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        
        for s in strs:
            sorting = sorted(s)
            sorted_s = ''.join(sorting)
            mp[sorted_s].append(s)

        return list(mp.values())