class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [i * -1 for i in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            add = first - second
            if add == 0:
                continue
            heapq.heappush(stones, add)
        return stones[0] * -1 if stones else 0