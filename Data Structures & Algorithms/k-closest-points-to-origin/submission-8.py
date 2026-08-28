class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for point in points:
            x,y = point[0], point[1]
            dist = x ** 2 + y ** 2
            minHeap.append([dist, x, y])
        heapq.heapify(minHeap)
        
        res = []
        while k > 0:
            x = heapq.heappop(minHeap)
            res.append(x[1:])
            k -= 1
        return res
        


