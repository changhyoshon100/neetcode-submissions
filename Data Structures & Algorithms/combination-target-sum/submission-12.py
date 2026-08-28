class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        def dfs(i, total, res):
            nonlocal ans
            if total > target or i == len(nums):
                return 
            if total == target:
                ans.append(res.copy())
                return 
            
            res.append(nums[i])
            total += nums[i]
            dfs(i, total, res)
            res.pop()
            total -= nums[i]
            dfs(i+1, total, res)
        
        dfs(0, 0, [])
        return ans