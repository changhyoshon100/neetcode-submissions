class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        for s in strs:
            sorted_s = sorted(s)
            key = ''.join(sorted_s)

            mp[key].append(s)
        return list(mp.values())

