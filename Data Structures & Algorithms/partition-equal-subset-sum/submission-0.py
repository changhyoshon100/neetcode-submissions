class Solution:
    def canPartition(self, nums: List[int]) -> bool:
# dfs sometimes returns None (because you return with no value). 
# Then the result becomes None instead of True/False.

# You don’t stop when i goes out of bounds.

# You call dfs(add + nums[i], ...) twice, and the second time you increment i 
# manually in a confusing way.

# return dfs(0,0) if True else False always returns dfs(0,0) (the if True is meaningless).

# Also you must check sum(nums) is even; otherwise it’s impossible.
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums)
        def dfs(curr, i):
            if i >= len(nums):
                return False
            if curr > target // 2:
                return False
            if curr == target // 2:
                return True
            return dfs(curr + nums[i], i+1) or dfs(curr, i+1)

        
        return dfs(0, 0)
