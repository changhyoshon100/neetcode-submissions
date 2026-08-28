class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        comparison = sorted(set(nums))
        nums[:len(nums)] = comparison
        return len(nums)