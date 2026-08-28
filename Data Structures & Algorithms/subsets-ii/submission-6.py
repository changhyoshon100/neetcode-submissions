class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums.sort()
        def dfs(i, res):
            nonlocal ans
            if i == len(nums):
                ans.add(tuple(res.copy()))
                return 
            
            res.append(nums[i])
            dfs(i+1, res)
            res.pop()
            dfs(i+1, res)

        dfs(0, [])
        return list(ans)