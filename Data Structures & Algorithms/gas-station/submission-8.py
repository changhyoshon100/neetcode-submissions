class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        res = 0
        start = 0
        L = 0
        
        if sum(gas) < sum(cost): return -1
        for R in range(len(gas)):
            res += (gas[R] - cost[R])    
            if res < 0:
                L = R + 1
                res = 0
        return L
