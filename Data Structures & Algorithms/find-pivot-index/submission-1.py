class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        num_sum = sum(nums)
        L = 0
        left_sum = 0
        suffix = num_sum
        prefix = 0
        if prefix + nums[0] == suffix:
            return 0
        
        while L < len(nums) - 1:
            prefix += nums[L]
            suffix = num_sum - prefix
            if prefix + nums[L+1] == suffix:
                return L + 1
            suffix = num_sum
            L += 1

        return -1