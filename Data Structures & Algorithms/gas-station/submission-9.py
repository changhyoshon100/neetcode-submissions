class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): return -1
        res = 0
        ans = 0
        for i in range(len(gas) - 1):
            res += (gas[i] - cost[i])
            if res < 0:
                res = 0
                ans = i + 1
        return ans