class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minVal = prices[0]
        res = 0
        j = 0
        for i in range(len(prices) - 1):
            minVal = min(minVal, prices[i])
            if minVal == prices[i]:
                j = i+1   
            res = max(max(prices[j:len(prices)]) - minVal, res)
            print(res,minVal)
        return 0 if res <= 0 else res
            
