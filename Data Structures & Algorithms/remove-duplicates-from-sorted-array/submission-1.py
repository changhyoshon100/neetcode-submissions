class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = set(sorted(nums))
        nums[:] = sorted(unique)
        return len(nums)