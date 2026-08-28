class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        arr = []
        for x,y in points:
            dist = (x**2) + (y**2)
            arr.append([dist, x,y])
        
        heapq.heapify(arr)
        while k > 0:
            dist,x,y = heapq.heappop(arr)
            res.append([x,y])
            k -= 1
        return res

