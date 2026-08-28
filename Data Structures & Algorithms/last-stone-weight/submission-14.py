class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        negStones = [stones[i]*-1 for i in range(len(stones))]
        heapq.heapify(negStones)
        while len(negStones) >= 2:
            x,y = heapq.heappop(negStones), heapq.heappop(negStones)
            heapq.heappush(negStones, x - y)
            # print(negStones)
        return -negStones[0] 
