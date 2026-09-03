class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        for p in points:
            x,y = p
            dist = math.sqrt(x ** 2 + y ** 2)
            res.append([dist, (x,y)])
        heapq.heapify(res)
        ans = []
        while len(ans) < k:
            ans.append(heapq.heappop(res)[1])
        return ans
        
            
