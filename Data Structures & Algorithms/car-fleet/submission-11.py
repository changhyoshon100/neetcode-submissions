class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        for p,s in zip(position, speed):
            stack.append((p,s))
        stack.sort()
        
        res = []
        for i in range(len(position)):
            p, s = stack.pop()
            time = (target - p) / s
            if res and res[-1] >= time:
                continue
            res.append(time)
            
        return len(res)
