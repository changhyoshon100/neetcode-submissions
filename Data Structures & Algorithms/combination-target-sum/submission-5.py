class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        curr, subset = [], []
        
        def dfs(i, curr, subset):
            val = sum(curr)
            if i >= len(nums):
                return
            if val == target:
                subset.append(curr.copy())
                return
            if val > target:
                return
            
            curr.append(nums[i])
            dfs(i, curr, subset)
            curr.pop()
            dfs(i+1, curr, subset)
            
        dfs(0, curr, subset)
        return subset
