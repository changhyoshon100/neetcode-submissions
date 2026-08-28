class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def dfs(i, res):
            nonlocal ans
            if i == len(nums):
                cp = res.copy()
                ans.append(cp)
                return ans

            res.append(nums[i])
            dfs(i+1, res)
            res.pop()
            dfs(i+1, res)

        dfs(0, [])
        return ans