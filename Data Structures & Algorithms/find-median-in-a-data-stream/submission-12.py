class MedianFinder:

    def __init__(self):
        self.plus = []
        heapq.heapify(self.plus)
        self.minus = []
        heapq.heapify(self.minus)

    def addNum(self, num: int) -> None:
        if self.plus:
            x = 0
            if num > self.plus[0]:
                x = heapq.heappop(self.plus)
                heapq.heappush(self.minus, x * -1)
                heapq.heappush(self.plus, num)
            else:
                x = num
                heapq.heappush(self.plus, num)
        
        if len(self.plus) >= len(self.minus) + 1:
            x = heapq.heappop(self.plus)
            heapq.heappush(self.minus, x * -1)
        
        if len(self.minus) >= len(self.plus) + 1:
            x = heapq.heappop(self.minus)
            heapq.heappush(self.plus, x * -1)

        if not self.plus:
            heapq.heappush(self.plus, num)
        # print(num, self.minus, self.plus)
        
    def findMedian(self) -> float:
        if len(self.plus) > len(self.minus):
            return self.plus[0]
        if len(self.minus) > len(self.plus):
            return self.minus[0] * -1
        if self.plus and self.minus:
            return (self.plus[0] + self.minus[0] * -1) / 2
        
        