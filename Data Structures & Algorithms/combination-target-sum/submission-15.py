class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i,total,sub):
            nonlocal res
            if total == target:
                res.append(sub.copy())
                return res
            if total > target:
                return 0
            if i == len(nums):
                return 0
            
            sub.append(nums[i])
            dfs(i, total + nums[i], sub)
            sub.pop()
            dfs(i+1, total, sub)

        dfs(0,0,[])
        return res