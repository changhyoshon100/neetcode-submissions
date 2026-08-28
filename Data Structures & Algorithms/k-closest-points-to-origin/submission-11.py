class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(arr):
            x = arr[0]
            y = arr[1]
            dist = math.sqrt(x**2 + y**2)
            return [round(dist, 3),x,y]
        
        arr = []
        for x1, y1 in points:
            [dist,corx,cory] = distance([x1,y1])
            arr.append([dist,corx,cory])
        heapq.heapify(arr)
        
        res = []
        for i in range(k):
            x = heapq.heappop(arr)
            res.append(x[1:])
            
        return res
        