class Solution:
    def canJump(self, nums: List[int]) -> bool:
        start = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if start <= nums[i] + i:
                start = i
        return start == 0