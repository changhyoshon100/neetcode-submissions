class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, num * -1)

        if self.small and self.large and self.small[0] * -1 > self.large[0]:
            x = heapq.heappop(self.small)
            heapq.heappush(self.large, x * -1)
        
        if len(self.small) > len(self.large) + 1:
            y = heapq.heappop(self.small)
            heapq.heappush(self.large, y * -1)
        
        if len(self.large) > len(self.small) + 1:
            y = heapq.heappop(self.large)
            heapq.heappush(self.small, y * -1)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return self.small[0] * -1
        elif len(self.small) < len(self.large):
            return self.large[0]
        else:
            return (self.small[0] * -1 + self.large[0]) / 2
        
        