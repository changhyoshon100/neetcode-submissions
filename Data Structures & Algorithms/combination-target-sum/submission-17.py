class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, total, subsets):
            if total == target:
                cp = subsets.copy()
                res.append(cp)
                return
            if i == len(nums) or total > target:
                return 
            
            subsets.append(nums[i])
            dfs(i, total + nums[i], subsets)
            subsets.pop()
            dfs(i+1, total, subsets)
            
        dfs(0, 0, [])
        return res