class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        if self.large and self.large[0] < num:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -1 * num)
        
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large) 
            heapq.heappush(self.small, -1 * val)
        

    def findMedian(self) -> float:
        if len(self.large) < len(self.small):
            return self.small[0] * -1
        if len(self.small) < len(self.large):
            return self.large[0]
        return (self.large[0] + self.small[0] * -1) / 2.0

        
        