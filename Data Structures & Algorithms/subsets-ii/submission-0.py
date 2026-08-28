class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        curr, sub = [], []
        def helper(nums, i, curr, sub):
            if i >= len(nums):
                cp = curr.copy()
                sub.append(cp)
                return
            
            curr.append(nums[i])
            helper(nums, i+1, curr, sub)
            curr.pop()
            
            while i <= len(nums)-1 and nums[i] == nums[min(i+1, len(nums)-1)]:
                i += 1
            helper(nums, i+1, curr, sub)
        
        helper(nums, 0, curr, sub)
        return sub
