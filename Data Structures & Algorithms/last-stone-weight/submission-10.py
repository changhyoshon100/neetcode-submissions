class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        s = [-s for s in stones]
        heapq.heapify(s)
        while len(s) > 1:
            x = heapq.heappop(s)
            y = heapq.heappop(s)
            heapq.heappush(s, x - y)
        return abs(s[0])