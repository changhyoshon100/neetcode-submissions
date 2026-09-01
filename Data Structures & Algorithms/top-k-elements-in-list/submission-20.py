class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = defaultdict(int)
        for i,v in enumerate(nums):
            mp[v] += 1
        # print(mp)
        res = []
        
        for v,i in mp.items():
            res.append((i,v))
        
        res.sort()
        # print(res)
        ans = []
        while res and len(ans) < k:
            ans.append(res.pop()[1])
        # print(ans)
        return ans
        
            