class Solution:
    def findMin(self, nums: List[int]) -> int:
        L, R = 0, len(nums) - 1
        while L < R:
            mid = (L + R) // 2
            if nums[mid] < nums[R]:
                # minimum is right or mid itself
                R = mid
            else:
                # nums[mid] > nums[R]
                # minimum is left
                L = mid + 1
        return nums[L]