class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subsets = []
        def dfs(i, total):
            if i >= len(nums):
                return 
            if total > target:
                total -= nums[i]
                return 
            if total == target:
                res.append(subsets.copy())
                return 

            subsets.append(nums[i])
            dfs(i, total + nums[i])
            i+=1
            subsets.pop()
            dfs(i, total)
            return res
        return dfs(0, 0)
        

