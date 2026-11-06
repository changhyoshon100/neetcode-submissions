class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        res = []
        output = [0] * len(t)

        for i,v in enumerate(t):
            while res and res[-1][1] < v:
                idx, val = res.pop()
                output[idx] = (i - idx)
            res.append((i,v))
        return output
