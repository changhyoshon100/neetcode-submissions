class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        res = []
        for p,s in zip(position, speed):
            res.append((p,s))
        res = sorted(res)[::-1]
        
        for i in range(len(res)):
            
            time = (target - res[i][0]) / res[i][1]
            if stack and stack[-1] >= time:
                # print(stack)
                # stack.pop()
                continue
            else:
                stack.append((time))
            
            
        return len(stack)