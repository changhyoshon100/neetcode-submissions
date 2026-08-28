class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = defaultdict(int)
        for i,v in enumerate(nums):
            mp[v] += 1

        res = []
        for val, cnt in mp.items():
            res.append([cnt, val])
        res.sort()
        
        ans = []
        while len(ans) < k:
            ans.append(res.pop()[-1])
        return ans
            