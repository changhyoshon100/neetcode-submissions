class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        bucket = set()
        
        def dfs(arr, i):
            if i == len(arr):
                bucket.add(tuple(res.copy()))
                return bucket
            
            res.append(arr[i])
            dfs(arr, i+1)
            res.pop()
            dfs(arr, i+1)
            return bucket
        
        return list(dfs(nums, 0))