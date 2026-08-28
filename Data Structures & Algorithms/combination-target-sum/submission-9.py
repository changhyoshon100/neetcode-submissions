class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        arr = []
        res = []
        def dfs(nums, i, val):
            if val == target:
                return res.append(arr.copy())
            if val > target:
                return 
            if i == len(nums):
                return 
                
            val += nums[i]
            arr.append(nums[i])
            dfs(nums, i, val)
            minus = arr.pop()
            val -= minus
            dfs(nums, i+1, val)

        dfs(nums, 0, 0)
        return res