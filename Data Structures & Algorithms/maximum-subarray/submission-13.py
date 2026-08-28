class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = float('-inf')
        large = 0
        for n in nums:
            large = large + n 
            total = max(total, large)
            
            if large < 0:
                large = 0
            
                
        return total
