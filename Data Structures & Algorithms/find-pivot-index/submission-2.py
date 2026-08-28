class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        L, R = 0, len(nums) - 1
        total = sum(nums)
        l_total = 0
        for i in range(len(nums)):
            total -= nums[i]
            if total == l_total:
                return i
            l_total += nums[i]
        return -1