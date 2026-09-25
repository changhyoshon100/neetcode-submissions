class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        left = 0
        profit = 0

        for right in range(1, len(prices)):
            if prices[right] >= prices[right - 1]:
                profit = prices[right] - prices[left]
            else:
                total += profit
                profit = 0
                left = right

        return total + profit