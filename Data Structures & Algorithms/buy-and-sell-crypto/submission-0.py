class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        maxP = 0
        for R in range(len(prices)):
            value = prices[L] - prices[R]
            if value > 0:
                L = R
            else:
                maxP = max(maxP, abs(value))
        return maxP
                
                

            
            