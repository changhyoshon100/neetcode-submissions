class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        bucket = []
        def dfs(arr, i):
            if i == len(arr):
                bucket.append(res.copy())
                return 
            
            res.append(arr[i])
            dfs(arr, i+1)
            res.pop()
            dfs(arr, i+1)
            return bucket

        return dfs(nums, 0)