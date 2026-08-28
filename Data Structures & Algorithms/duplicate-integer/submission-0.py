class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return True if len(list(set(nums))) != len(nums) else False