class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = [-nums[i] for i in range(len(nums))]
        print(nums)
        heapq.heapify(minHeap)
        ans = 0
        print(minHeap)
        while k > 0:
            k -= 1
            ans = heapq.heappop(minHeap)
        return -ans
        
