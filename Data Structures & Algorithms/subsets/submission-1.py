class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.dfs([],[], nums, 0)
    def dfs(self, res, subsets, nums, i):
        if i >= len(nums):
            res.append(subsets.copy())
            return 
        subsets.append(nums[i])
        self.dfs(res, subsets, nums, i+1)
        subsets.pop()
        self.dfs(res, subsets, nums, i+1)
        return res

