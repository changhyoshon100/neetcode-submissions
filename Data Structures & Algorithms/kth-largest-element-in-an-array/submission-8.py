class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = [-1 * i for i in nums]
        heapq.heapify(minHeap)
        
        for i in range(k-1):
            heapq.heappop(minHeap)
        return minHeap[0] * -1