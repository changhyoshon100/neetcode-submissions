class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        
        for i in range(len(strs)):
            sort_st = sorted(strs[i])
            join_st = ''.join(sort_st)
            
            if join_st not in mp:
                mp[join_st] = [strs[i]]
            else:
                mp[join_st].append(strs[i])
        
        return list(mp.values())