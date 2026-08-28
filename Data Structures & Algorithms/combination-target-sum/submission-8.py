class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        arr = []
        ans = []
        def dfs(i, res):
            if i >= len(nums) or res > target:
                return
            if res == target:
                ans.append(arr.copy())
                return
            
            res += nums[i]
            arr.append(nums[i])
            dfs(i, res)
            res -= nums[i]
            arr.pop()
            dfs(i+1, res)

        dfs(0, 0)
        return ans