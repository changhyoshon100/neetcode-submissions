class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = defaultdict(int)
        for n in nums:
            mp[n] += 1
        res = []
        
        ans = []
        for key, cnt in mp.items():
            res.append([cnt, key])
       
        res.sort()
        while len(ans) < k:
            ans.append(res.pop()[1])
        
        return ans