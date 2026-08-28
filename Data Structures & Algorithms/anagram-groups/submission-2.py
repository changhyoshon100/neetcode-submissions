class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        for s in strs:
            s_sorted = sorted(s)
            str_sorted = ''.join(s_sorted)
            mp[str_sorted].append(s)
        return list(mp.values())
            
