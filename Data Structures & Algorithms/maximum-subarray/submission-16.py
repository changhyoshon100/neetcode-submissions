class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        large = 0
        total = float('-inf')

        for n in nums:
            large += n
            total = max(large, total)

            if large < 0:
                large = 0
                
        return total