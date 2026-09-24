class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(i,sub):
            nonlocal res
            if i == len(nums):
                return res.append(sub.copy())
            
            dfs(i+1,sub)
            sub.append(nums[i])
            dfs(i+1,sub)
            sub.pop()
        
        dfs(0,[])
        return res