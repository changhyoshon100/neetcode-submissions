class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        cnt = 0
        for i in range(len(temperatures)):
            pivot = temperatures[i]
            cnt = 0
            for j in range(i, len(temperatures)):
                if pivot < temperatures[j]:
                    stack.append(cnt)
                    break
                cnt += 1
                if j == len(temperatures)-1:
                    stack.append(0)
        return stack
            
                


                
