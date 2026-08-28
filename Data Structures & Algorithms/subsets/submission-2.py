class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        curr, sub = [], []

        def helper(i, nums, curr, sub):
            if i >= len(nums):
                cp = curr.copy()
                sub.append(cp)
                return 
            
            curr.append(nums[i])
            helper(i+1, nums, curr, sub)
            curr.pop()
            helper(i+1, nums, curr, sub)

        helper(0, nums, curr, sub)
        return sub
        