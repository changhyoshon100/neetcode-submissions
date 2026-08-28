class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        leng = len(nums)
        leng2 = len(set(nums))
        return leng != leng2