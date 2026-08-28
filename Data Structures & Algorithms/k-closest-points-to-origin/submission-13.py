class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(arr):
            x1, y1 = arr[0], arr[1]
            dist = math.sqrt(x1 ** 2 + y1 ** 2)
            return dist

        minHeap = []
        for x1,y1 in points:
            dist = distance([x1,y1])
            minHeap.append([dist, x1, y1])
        
        heapq.heapify(minHeap)
        res = []
        for i in range(k):
            a = heapq.heappop(minHeap)
            res.append(a[1:])
        return res
