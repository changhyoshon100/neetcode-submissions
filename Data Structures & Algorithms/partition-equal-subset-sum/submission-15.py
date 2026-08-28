class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums) 
        if total % 2 != 0:
            return False
        memo = {}
        total = total // 2
        def dfs(i, value):
            if value == total:
                return True
            if i == len(nums) or value > total:
                return False
            if (i,value) in memo:
                return memo[(i,value)]
            
            a = dfs(i+1, value + nums[i])
            b = dfs(i+1, value)
            memo[(i,value)] = a or b

            return memo[(i,value)]

        return dfs(0,0)
