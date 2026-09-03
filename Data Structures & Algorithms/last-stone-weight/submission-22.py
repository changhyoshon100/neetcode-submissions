class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [i * -1 for i in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            a = heapq.heappop(stones)
            b = heapq.heappop(stones)
            heapq.heappush(stones, (a - b))
        
        return stones[0] * -1