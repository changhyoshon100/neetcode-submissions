class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # without sort => max-heap
        # python default is min-heap using - to make max heap

        heap = []
        for num in nums:
            heapq.heappush(heap, -num)

        ans = 0
        while k > 0:
            ans = -heapq.heappop(heap)
            k -= 1

        return ans