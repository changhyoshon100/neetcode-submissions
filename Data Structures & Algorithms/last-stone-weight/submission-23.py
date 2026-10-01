class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)

        while len(heap) > 1:
            stoneX = -heapq.heappop(heap)
            stoneY = -heapq.heappop(heap)

            if stoneX != stoneY:
                heapq.heappush(heap, -abs(stoneX - stoneY))

        return -heapq.heappop(heap) if len(heap) == 1 else 0