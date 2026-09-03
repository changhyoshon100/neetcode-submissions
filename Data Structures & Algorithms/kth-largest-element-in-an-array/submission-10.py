class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        
        while len(nums)-1 >= k:    
            heapq.heappop(nums)
        
        return nums[0]
