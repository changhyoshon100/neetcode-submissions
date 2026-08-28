class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        minHeap = []
        for i in range(len(nums)):
            mp[nums[i]] += 1
        
        for i in range(len(mp.values())):
            heapq.heappush(minHeap, [-mp[nums[i]], -nums[i]])
        val = heapq.heappop(minHeap)
        return -val[1]
        

        
        
