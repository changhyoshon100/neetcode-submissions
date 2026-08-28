class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L = 0
        for R in range(1, len(nums)):
            if nums[L] != nums[R]:
                nums[L+1] = nums[R]
                L += 1
        return L + 1
