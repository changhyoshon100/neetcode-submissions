class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = set(nums)
        nums[:] = sorted(unique)
        return len(nums)