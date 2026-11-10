class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def dfs(i, subsets):
            if i == len(nums):
                cp = subsets.copy()
                res.append(cp)
                return
            
            subsets.append(nums[i])
            dfs(i+1, subsets)
            subsets.pop()
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1, subsets)
            
        dfs(0, [])
        return res