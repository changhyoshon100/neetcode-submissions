class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        bucket = []
        def dfs(arr, i):
            if i >= len(arr):
                return 0
            if target < sum(res):
                return 0
            if target == sum(res):
                return bucket.append(res.copy())

            res.append(arr[i])
            dfs(arr, i)
            res.pop()
            dfs(arr, i+1)
            return bucket
        
        return dfs(nums, 0)