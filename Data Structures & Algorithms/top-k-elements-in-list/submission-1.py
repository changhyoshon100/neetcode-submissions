class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = defaultdict(int)
        for i,v in enumerate(nums):
            mp[v] += 1
        arr = []
        sorted_mp = dict(sorted(mp.items(), key=lambda item: item[1]))
        
        return list(sorted_mp.keys())[-k:]
            