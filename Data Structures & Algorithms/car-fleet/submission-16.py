class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        zip_arr = []
        for i in range(len(position)):
            zip_arr.append((position[i], speed[i]))
        
        zip_arr.sort()
        res = []
        for i in range(len(position)):
            p, s = zip_arr.pop()
            time = (target - p) / s
            
            if res and res[-1] >= time:
                continue

            res.append(time)
        return len(res)
        
