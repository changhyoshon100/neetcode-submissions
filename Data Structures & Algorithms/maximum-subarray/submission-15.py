class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = float('-inf')
        large = 0
        for n in nums:
            large += n
            total = max(large, total)
            
            if large < 0:
                large = 0
            
        return total