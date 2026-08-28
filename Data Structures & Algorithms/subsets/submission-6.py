class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        arr = []
        res = []
        def dfs(nums, i):
            if i == len(nums):
                res.append(arr.copy())
                return
            arr.append(nums[i])
            dfs(nums, i+1)
            arr.pop()
            dfs(nums, i+1)

        dfs(nums, 0)
        return res