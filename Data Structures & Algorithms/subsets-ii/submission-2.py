class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        arr = []
        res = []
        visit = set()
        def dfs(arr, i):
            if i == len(nums):
                if sorted(arr) in res:
                    return 
                res.append(sorted(arr.copy()))
                return
            

            arr.append(nums[i])
            dfs(arr, i+1)
            arr.pop()
            dfs(arr, i+1)
        
        dfs(arr, 0)
        return res