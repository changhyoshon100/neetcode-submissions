class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = []
        xy_arr = []
        dic = {}
        def uclidian(points, k,xy_arr):
            for x,y in enumerate(points):
                print('hi',y[0],y[1])
                print('--')
                dist = math.sqrt(y[0]**2 + y[1]**2)

                dist = round(dist,3)
                xy_arr.append(dist)
                print((xy_arr))
                if dist not in dic: dic[dist] = [(y[0],y[1])]
                else:
                    dic[dist].append((y[0],y[1]))
                print(dic)

                if len(xy_arr) > k:
                    xy_arr = [-s for s in xy_arr]
                    print('heapq bf',xy_arr)
                    heapq.heapify(xy_arr)
                    print('heapq',xy_arr)
                    
                    heapq.heappop(xy_arr)
                    xy_arr = [-s for s in xy_arr]
                    print('xy_arr',xy_arr)
            arr = []
            print('##',xy_arr)
            print('dic',dic)
            for xy in xy_arr:
                print('@@',xy)
                for inner in dic[xy]:
                    print('inner', inner)
                    if len(arr) < k:
                        arr.append(list(inner))
            print(xy_arr)
            return arr
                    
        return uclidian(points, k,xy_arr)
        
                    
                    








