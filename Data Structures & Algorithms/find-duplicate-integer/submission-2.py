class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        visit = set()
        for i in range(len(nums)):
            if nums[i] in visit:
                return nums[i]
            visit.add(nums[i])
            