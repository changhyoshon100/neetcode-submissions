class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        bucket = []
        def dfs(arr, i, total):
            if i >= len(arr):
                return 0
            if target < total:
                return 0
            if target == total:
                return bucket.append(res.copy())
            
            total += arr[i]
            res.append(arr[i])
            dfs(arr, i, total)
            val = res.pop()
            total -= val
            dfs(arr, i+1, total)
            return bucket
        
        return dfs(nums, 0, 0)