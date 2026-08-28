class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i,v in enumerate(temperatures):
            while stack and stack[-1][0] < v:
                stackVal, stackIdx = stack.pop()
                res[stackIdx] = i - stackIdx
            stack.append([v, i])
        return res