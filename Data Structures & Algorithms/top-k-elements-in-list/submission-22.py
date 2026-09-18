class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = defaultdict(int)
        for i in range(len(nums)):
            mp[nums[i]] += 1
        
        minHeap = []

        for v,i in sorted(mp.items()):
            heapq.heappush(minHeap, [i * -1, v])
        
        res = []
        while len(res) < k:
            res.append(heapq.heappop(minHeap)[1])
        return res