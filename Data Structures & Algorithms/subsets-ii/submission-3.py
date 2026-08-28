class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(nums, i, arr):
            if i == len(nums):
                if arr in res:
                    return
                res.append(arr.copy())
                return
            
            arr.append(nums[i])
            dfs(nums, i+1, arr)
            arr.pop()
            dfs(nums, i+1, arr)

        dfs(nums, 0, [])
        return res