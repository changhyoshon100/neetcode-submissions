class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        for p,s in zip(position, speed):
            stack.append((p,s))
        
        stack.sort()
        res = []
        # print(stack)
        while stack:
            pos, sp = stack.pop()
            time = (target - pos) / sp
            
            if res and res[-1] >= time:
                continue
            res.append(time)
        return len(res)





