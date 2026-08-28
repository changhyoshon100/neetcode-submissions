class Solution:
    def rob(self, nums: List[int]) -> int:
        mp = {}
        
        def dfs(i, res, n):
            if i >= n:
                return 0
            if i in mp:
                return mp[i]
            
            mp[i] = max(nums[i] + dfs(i+2, res, n), dfs(i+1, res, n))
            return mp[i]

        return dfs(0,0, len(nums))