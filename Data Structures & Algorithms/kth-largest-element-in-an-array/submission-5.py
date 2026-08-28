class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr = [i for i in nums]
        heapq.heapify(arr)
        
        while len(arr) > k:
            heapq.heappop(arr)
        return arr[0]