class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones: return 0
        if len(stones) < 2:
            return stones[0]
        minHeap = [stones[i] * -1 for i in range(len(stones))]
        heapq.heapify(minHeap)
        
        while len(minHeap) > 1:
            a = heapq.heappop(minHeap)
            b = heapq.heappop(minHeap)
            if a == b:
                continue
            new = abs(b - a)
            heapq.heappush(minHeap, new * -1)
            
        return -minHeap[0] if minHeap else 0

