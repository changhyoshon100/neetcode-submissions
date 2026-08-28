class Solution:
    def rob(self, nums: List[int]) -> int:
        maximum = 0
        rob = 0
        cache = {}
        def dfs(i, rob):
            if i >= len(nums):
                return 0
            if i in cache:
                return cache[i]

   
            cache[i] = max(nums[i] + dfs(i+2, rob) , dfs(i+1, rob))
            return cache[i]
            
 
        return dfs(0, 0)