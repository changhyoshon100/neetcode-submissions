class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        s = [-s for s in nums]
        heapq.heapify(s)
        while k > 1:
            heapq.heappop(s)
            k -= 1
        return -s[0]