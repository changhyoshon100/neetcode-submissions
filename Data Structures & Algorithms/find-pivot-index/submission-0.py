class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalLeft = 0
        total = sum(nums)
        
        if total - nums[0] == 0:
            return 0
        for i in range(1,len(nums)):
            totalLeft += nums[i-1]
            rem = total - totalLeft - nums[i]
            if totalLeft == rem:
                return i
            else:
                rem = total
        return -1